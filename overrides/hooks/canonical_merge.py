"""Simple hook to merge 2 build directories.

It expects the default `site` directory as source for the other files.
It also adjusts canonical URL values of pages.

MIT Licence 2024 Kamil Krzyśków (HRY) for Nype (npe.cm) and Fiori Tracker (fioritracker.org)
"""

from pathlib import Path

import shutil

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import event_priority
from mkdocs.structure.pages import Page


OLD_PREFIX: str = "V2020/"
SITEMAP_REDIRECT_MAP: dict[str, str] = {}
ENABLED = False


def on_startup(command, dirty):
    global ENABLED
    ENABLED = command != "serve"


def on_config(config):
    SITEMAP_REDIRECT_MAP.clear()


def on_page_markdown(markdown, page: Page, config: MkDocsConfig, files):
    """The pages need to have proper rel=canonical values"""

    if not ENABLED:
        return

    site_url = config.site_url.rstrip("/") + "/"

    new_version = True
    if "for_deploy" in config.config_file_path:
        new_version = False

    # The page paths where the rel=canonical will point to the new version.
    # rel=canonical in all other pages will point to the old version.
    canonical_paths = ["core/SPS02/main", "tracked/SPS03/roles", "cr/SPS02/main"]

    # New version with clean path https://base_url/
    if new_version:
        for path in canonical_paths:
            if path in page.canonical_url:
                # Only one path is enough to exclude
                break

            assert OLD_PREFIX not in page.canonical_url
            new_canonical = page.canonical_url.replace(site_url, site_url + OLD_PREFIX)
            assert page.canonical_url != new_canonical

            page.canonical_url = new_canonical
            SITEMAP_REDIRECT_MAP[page.url] = page.canonical_url

            # Process the canonical_url once
            break
    # Old version with prefixed path https://base_url/V2020/
    else:
        for path in canonical_paths:
            if path not in page.canonical_url:
                # All paths need to be checked to exclude
                continue

            assert OLD_PREFIX in page.canonical_url
            new_canonical = page.canonical_url.replace(OLD_PREFIX, "", 1)
            assert page.canonical_url != new_canonical

            page.canonical_url = new_canonical
            SITEMAP_REDIRECT_MAP[page.url] = page.canonical_url

            # Process the canonical_url once
            break


# Break convention of minimal -100
@event_priority(-105)
def on_post_build(config: MkDocsConfig):
    """Copy the files over making sure some files aren't overriden"""

    if not ENABLED:
        return

    deploy_site_dir = Path(config.site_dir)
    new_site_dir = deploy_site_dir.parent / "site"

    new_version = True
    if "for_deploy" in config.config_file_path:
        new_version = False

    # New version with default path doesn't need to copy anything
    if new_version:
        return

    old_version_with_prefix = deploy_site_dir / OLD_PREFIX.rstrip("/")
    new_version_with_prefix = new_site_dir / OLD_PREFIX.rstrip("/")

    # Move files for Google to find them on the old path
    shutil.move(str(deploy_site_dir / "sitemap.xml"), str(old_version_with_prefix))
    shutil.move(str(deploy_site_dir / "sitemap.xml.gz"), str(old_version_with_prefix))
    shutil.move(str(deploy_site_dir / "404.html"), str(old_version_with_prefix))

    # Due shutil.copytree not allowing to merge 2 directories, while setting the `exist_ok`
    # flag only to the root directory, this weird switch allows to detect copy errors as required.
    shutil.copytree(str(old_version_with_prefix), str(new_version_with_prefix))
    shutil.rmtree(str(deploy_site_dir))
    shutil.move(str(new_site_dir), str(deploy_site_dir))
