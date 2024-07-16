"""MkDocs hook to add SAP icons

The icons are taken from the https://github.com/SAP/ui5-webcomponents/ repository.
ICON_JSONS_URLS at the bottom of the file store URLs to fetch that contain JSON file with SVG paths.
Those paths are injected into a <svg> tag with a viewBox of 0 0 512 512

Additionally, there are Nype icons/emojis injected as well.

MIT Licence 2024 Kamil Krzyśków (HRY) for Nype (npe.cm)
"""

import datetime as dt
import json
import logging
from pathlib import Path
from xml.etree.ElementTree import Element  # This is expected to be added by mkdocs-material

import requests  # This is expected to be added by mkdocs-material
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import PrefixedLogger


def on_config(config: MkDocsConfig):

    config_dir = Path(config.config_file_path).parent

    global CACHE_DIR, ICON_INDEXES
    CACHE_DIR = config_dir / ".cache" / "hooks" / HOOK_NAME

    if not config.mdx_configs.get("pymdownx.emoji"):
        return

    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    if not ICON_INDEXES:
        download_icons()
        add_nype_icons()
        load_indexes()
    else:
        LOG.info("Reuse already loaded indexes (restart MkDocs to reload)")

    index_func = config.mdx_configs["pymdownx.emoji"]["emoji_index"]
    config.mdx_configs["pymdownx.emoji"]["emoji_index"] = emoji_decorator(index_func)

    generator_func = config.mdx_configs["pymdownx.emoji"]["emoji_generator"]
    config.mdx_configs["pymdownx.emoji"]["emoji_generator"] = emoji_decorator(generator_func)


def emoji_decorator(func):

    if func.__name__.endswith("wrapper"):
        return func

    def index_wrapper(options, md):
        emoji_index = func(options, md)

        global MATERIAL_INDEX_UPDATED

        if not MATERIAL_INDEX_UPDATED:
            for index in ICON_INDEXES:
                emoji_index["emoji"].update(index)
            MATERIAL_INDEX_UPDATED = True
            LOG.info("Updated icon index with new icons")

        return emoji_index

    def generator_wrapper(index, shortname, alias, uc, alt, title, category, options, md):
        if shortname.startswith(NEW_ICON_PREFIX):
            icons = md.inlinePatterns["emoji"].emoji_index["emoji"]
            el = Element("span", {"class": options.get("classes", index)})
            el.text = md.htmlStash.store(
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">'
                + f'<path d="{icons[shortname]["svg_path"]}"></path>'
                + "</svg>"
            )
            return el

        return func(index, shortname, alias, uc, alt, title, category, options, md)

    if func.__name__ == "twemoji":
        return index_wrapper
    else:
        return generator_wrapper


def add_nype_icons():

    # TODO load it from overrides directory, perhaps change it to a file path lookup
    custom_index = {
        ":ext-nype-logo:": {
            "svg_path": "m508 216.2c-0.2-3.9-1.1-7.7-2.7-11.3-1.5-3.5-3.8-6.8-6.6-9.5-2.8-2.7-6.1-4.8-9.7-6.3-3.6-1.5-7.5-2.3-11.4-2.3h-139.4l63.6 237.5 104.4-196.8h-0.1q0.5-1.4 0.9-2.8 0.4-1.3 0.6-2.8 0.3-1.4 0.3-2.8 0.1-1.4 0.1-2.9zm-501.2 66.5v0.1q-0.7 1.5-1.3 3.1-0.5 1.6-0.9 3.3-0.3 1.6-0.5 3.3-0.1 1.7-0.1 3.4c0.2 3.7 0.9 7.3 2.4 10.6 1.4 3.4 3.4 6.5 5.9 9.2 2.5 2.6 5.4 4.8 8.7 6.5 3.3 1.6 6.8 2.6 10.4 3h142.5l-63.7-237.5zm308.2-95.9l-31.8-85.6c-1.2-2.7-2.8-5.2-4.7-7.4-1.9-2.2-4.1-4.2-6.5-5.8-2.5-1.6-5.2-2.8-8-3.7-2.8-0.8-5.7-1.3-8.6-1.3h-130.3q-2 0.1-3.9 0.4-2 0.3-3.9 0.9-1.8 0.6-3.6 1.5-1.8 0.8-3.5 1.9l86.9 237.5 30.1 82.3c0.9 3.1 2.4 6 4.2 8.6 1.9 2.7 4.2 5 6.8 6.9 2.6 1.9 5.4 3.4 8.5 4.4 3.1 1.1 6.3 1.6 9.5 1.6h129.8q2.1 0 4.2-0.3 2-0.3 4.1-0.9 2-0.6 3.9-1.5 1.8-0.8 3.6-2l-86.9-237.5z"
        }
    }

    ICON_INDEXES.append(custom_index)


def load_indexes():
    for url in ICON_JSONS_URLS:
        filename = url.rsplit("/", 1)[-1]

        if DOWNLOAD_NEW_PER_WEEK:
            filename = f"{WEEK}-{filename}"

        filepath = CACHE_DIR / filename

        if not filepath.exists():
            LOG.error(f"File should exist at this point: {filepath}")
            continue

        with open(filepath, encoding="utf-8") as file:
            loaded = json.load(file)

        # we expect there to be a data structure with key -> dict pairs
        # skip if incompatible
        data = loaded.get("data")
        if not data:
            LOG.error(f"sap-icon pack has incompatible structure: {filepath}")
            continue

        new_data = {}

        # modify the data to prepare it for index merging
        for key in list(data.keys()):
            name = f"{NEW_ICON_PREFIX}{key.lower().strip()}:"
            new_data[name] = {"name": name, "svg_path": data[key]["path"]}
            del data[key]

        ICON_INDEXES.append(new_data)


def download_icons():
    for url in ICON_JSONS_URLS:
        filename = url.rsplit("/", 1)[-1]

        if DOWNLOAD_NEW_PER_WEEK:
            filename = f"{WEEK}-{filename}"

        filepath = CACHE_DIR / filename

        if filepath.exists():
            continue

        try:
            response = requests.get(url)
        except Exception as err:
            LOG.error(f"Failed to download {url}\n{err}")
            continue

        if response.status_code != 200:
            LOG.error(f"Failed to download {url}\nCode{response.status_code}")
            continue

        if not response.content:
            LOG.error(f"Despite a valid download, byte contents are empty\n{url}")

        filepath.write_bytes(response.content)

        LOG.info(f"Downloaded {filepath}")


HOOK_NAME: str = "sap_icons"
"""Name of the hook"""

CACHE_DIR: Path = None
"""Cache directory to put downloaded files, set later in event"""

DOWNLOAD_NEW_PER_WEEK: bool = True
"""Boolean to decide if the files should update after a week"""

WEEK: int = dt.datetime.now(dt.timezone.utc).isocalendar().week
"""Integer with the week value from ISO calendar"""

ICON_JSONS_URLS: list[str] = [
    "https://raw.githubusercontent.com/SAP/ui5-webcomponents/main/packages/icons/src/v5/SAP-icons.json"
]
"""List with links to JOSN files that contain SVG icon paths"""

ICON_INDEXES: list[dict[str, dict]] = []
"""Global list to store the indexes, filled later in event"""

LOG: PrefixedLogger = PrefixedLogger(HOOK_NAME, logging.getLogger(f"mkdocs.hooks.{HOOK_NAME}"))
"""Logger instance for this hook."""

MATERIAL_INDEX_UPDATED: bool = False
"""Boolean flag to keep track of index modification"""

NEW_ICON_PREFIX: str = ":ext-"
"""Prefix for the added icons to avoid overrides"""
