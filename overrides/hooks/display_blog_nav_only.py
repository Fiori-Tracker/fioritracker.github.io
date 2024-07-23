"""MkDocs hook to modify the display of the navigation items.

MIT Licence Kamil Krzyśków (HRY) for Nype (npe.cm) and Fiori Tracker (fioritracker.org)
"""

import logging

from material.plugins.blog.plugin import BlogPlugin
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import PrefixedLogger, event_priority
from mkdocs.structure.nav import Navigation


@event_priority(-75)
def on_nav(nav: Navigation, config: MkDocsConfig, files):
    """Run after blog plugin (-50). Gather 2 lists of nav entires that are inside and outside of the blog."""

    NON_BLOG_ENTRIES.clear()
    BLOG_ENTRIES.clear()

    blog_parent = None
    for name, instance in config.plugins.items():
        instance: BlogPlugin
        if name.startswith("material/blog"):
            if instance.config.blog_dir.strip("/") == BLOG_ROOT:
                blog_parent = instance.blog.parent

    if blog_parent is None:
        LOG.warning("blog parent not found")
        return nav

    for item in nav.items:
        if item is not blog_parent:
            NON_BLOG_ENTRIES.append(item)
        else:
            BLOG_ENTRIES.append(item)

    LOG.info("blog parent found")


def on_page_context(context, page, config: MkDocsConfig, nav: Navigation):
    """Repalce the nav for pages in the blog"""

    if not page.file.src_uri.startswith(BLOG_ROOT):
        nav.items = NON_BLOG_ENTRIES
    else:
        nav.items = BLOG_ENTRIES


HOOK_NAME: str = "display_blog_nav_only"
"""Name of the hook"""

LOG: PrefixedLogger = PrefixedLogger(HOOK_NAME, logging.getLogger(f"mkdocs.hooks.{HOOK_NAME}"))
"""Logger instance for this hook."""

NON_BLOG_ENTRIES = []
"""Non blog entries, filled in later"""

BLOG_ENTRIES = []
"""Blog entries, filled in later"""

BLOG_ROOT: str = "usecases"
"""blog_dir value to apply the instance"""
