"""Small CI script to shift docs files around and to adjust mkdocs.yml

That's the second iteration of "How to change directories around and not lose SEO ranking" strategy.
It works in unison with the `canonical_merge.py` hook.
It should be run in the root of the project.

MIT Licence 2024 Kamil Krzyśków (HRY) for Nype (npe.cm) and Fiori Tracker (fioritracker.org)
"""

from pathlib import Path
import re
import shutil
import sys


NEW_DOCS = "docs_for_deploy"
"""Name of the new docs directory"""

NEW_SITE = "site_for_deploy"
"""Name of the new site directory"""

NEW_CONFIG = "mkdocs_for_deploy.yml"
"""Name of the new config file"""

PREFIX_DIR = "V2020"
"""Name of the directory that is the new root"""


def main():
    """Entry point"""

    config_name = "mkdocs.yml"
    docs_dir_name = "docs"
    site_dir_name = "site"

    mkdocs_config = Path(config_name)

    if not mkdocs_config.exists():
        sys.exit(f"`{config_name}` config file not found in the CWD")

    docs_dir = Path(docs_dir_name)
    site_dir = Path(site_dir_name)

    if not docs_dir.exists():
        sys.exit(f"This script requires the docs={docs_dir} directory to have the docs files")

    if not site_dir.exists:
        sys.exit(
            f"This script needs to run after the site was built once, `{site_dir_name}` directory not found"
        )

    clear_path_and_copy_structure(old_docs=docs_dir, new_docs=Path(NEW_DOCS))
    process_config_and_save_new(mkdocs_config)


def clear_path_and_copy_structure(old_docs: Path, new_docs: Path):
    """Move files to the new structure"""

    docs_with_prefix = new_docs / PREFIX_DIR
    assets = docs_with_prefix / "assets"

    assert str(old_docs) != str(new_docs)

    if new_docs.exists():
        shutil.rmtree(str(new_docs))
    shutil.copytree(str(old_docs), str(docs_with_prefix))
    shutil.move(str(assets), str(new_docs))


def process_config_and_save_new(config: Path):
    """Adjust config for the new structure and save it in another file"""

    contents = config.read_text(encoding="utf-8")
    lines = contents.split("\n")
    prefix = f"{PREFIX_DIR}/"

    nav_re = re.compile(r":\s+(.*?\.md)")
    nav_re_subsection = re.compile(r"-\s+(.*?\.md)")  # For blog
    redirects_re = re.compile(r"'(.*?\.md)':\s+'(.*?\.md)'")

    new_docs = Path(NEW_DOCS)

    nav_region = False
    not_in_nav_region = False
    redirects_region = False
    redirects_override = False

    for i, line in enumerate(lines):
        # Single line changes
        if line.startswith("site_dir:"):
            lines[i] = line.replace(": site", ": site_for_deploy")
            continue

        if line.startswith("docs_dir:"):
            lines[i] = line.replace(": docs", ": docs_for_deploy")
            continue

        if "blog_dir:" in line:
            parts = line.split(": ")
            parts[1] = prefix + parts[1].lstrip()
            lines[i] = ": ".join(parts)

        # Conditionals for regions
        if line.startswith("nav:"):
            nav_region = True
            continue

        if "CI:nav" == line.strip("#").strip():
            nav_region = False
            continue

        if line.startswith("not_in_nav:"):
            not_in_nav_region = True
            continue

        if "CI:not_in_nav" == line.strip("#").strip():
            not_in_nav_region = False
            continue

        if line.lstrip().startswith("redirect_maps:"):
            redirects_region = True
            continue

        if "CI:redirects" == line.strip("#").strip():
            redirects_region = False
            continue

        # Logic for region
        if nav_region:
            regex = nav_re.search(line)
            if regex:
                lines[i] = line.replace(regex.groups()[0], prefix + regex.groups()[0])
            if ":" not in line:
                regex2 = nav_re_subsection.search(line)
                if regex2:
                    lines[i] = line.replace(regex2.groups()[0], prefix + regex2.groups()[0])

        if not_in_nav_region:
            lines[i] = line.replace("/", f"/{prefix}", 1)

        if redirects_region:
            regex = redirects_re.search(line)
            if regex:
                src_path = regex.groups()[0]
                dest_path = regex.groups()[1]
                entry_with_placeholders = line.replace(src_path, "SRC", 1).replace(
                    dest_path, "DEST", 1
                )
                if not (new_docs / src_path).exists():
                    # Clear other prefixes
                    if src_path.count("/") == 1 and src_path.endswith("index.md"):
                        lines[i] = f"#{line}"
                    else:
                        lines[i] = entry_with_placeholders.replace(
                            "SRC", prefix + src_path
                        ).replace("DEST", prefix + dest_path)
                    print("exists=False", src_path)
                else:
                    redirects_override = True
                    print("exists=True ", src_path)

    assert redirects_override is False
    Path(NEW_CONFIG).write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
