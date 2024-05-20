"""Small MkDocs hook, to modify the HTML template used in the redirects plugin

MIT Licence 2024 Kamil Krzyśków (HRY) for Fiori Tracker (fioritracker.org)
"""

import logging

from mkdocs.plugins import PrefixedLogger, event_priority

HOOK_NAME = "adjust_redirects_html"
LOG: PrefixedLogger = PrefixedLogger(HOOK_NAME, logging.getLogger(f"mkdocs.hooks.{HOOK_NAME}"))


@event_priority(100)
def on_config(config):

    if "redirects" not in config.plugins:
        LOG.warning("redirects plugin not found, hook should also be deleted")
        return
        
    import mkdocs_redirects.plugin as redirects
    
    old = '"noindex"'
    new = '"noindex, follow"'

    if new in redirects.HTML_TEMPLATE:
        LOG.debug("redirects plugin already patched, skipping...")
        return
     
    if old not in redirects.HTML_TEMPLATE:
        LOG.warning("redirects plugin HTML template not compatible with the patch")
        return
    
    redirects.HTML_TEMPLATE = redirects.HTML_TEMPLATE.replace(old, new)
    LOG.info("redirects HTML template was fixed")
