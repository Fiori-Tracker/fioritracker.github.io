"""Small MkDocs hook, to replace the HTML template used in the redirects plugin

MIT Licence 2024 Kamil Krzyśków (HRY) for Nype (npe.cm) and Fiori Tracker (fioritracker.org)
"""

import logging
import posixpath

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import PrefixedLogger, event_priority

HOOK_NAME = "adjust_redirects_html"
LOG: PrefixedLogger = PrefixedLogger(HOOK_NAME, logging.getLogger(f"mkdocs.hooks.{HOOK_NAME}"))

# Combined template of the mkdocs_redirect.plugin.HTML_TEMPLATE +
# https://github.com/squidfunk/mkdocs-material/blob/master/src/templates/redirect.html
# config.site_name needs to be filled in before overriding
# Also sets "noindex, follow"
HTML_TEMPLATE = """
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <title>{{ config.site_name }}</title>
    <link rel="canonical" href="{url}" />
    <meta name="robots" content="noindex, follow">
    <noscript>
      <meta http-equiv="refresh" content="0;url={url}" />
    </noscript>
    <script>
      window.location.replace([
        "{url}",
        window.location.search,
        window.location.hash
      ].join(""))
    </script>
  </head>
  <body></body>
</html>
"""


@event_priority(100)
def on_config(config: MkDocsConfig):

    if "redirects" not in config.plugins:
        LOG.warning("redirects plugin not found, hook should also be deleted")
        return

    import mkdocs_redirects.plugin as redirects

    redirects.HTML_TEMPLATE = HTML_TEMPLATE.replace("{{ config.site_name }}", config.site_name)
    redirects.write_html = write_html_wrapper(redirects.write_html, config)

    LOG.info("redirects HTML template was fixed for SEO")


def write_html_wrapper(func, config: MkDocsConfig):
    """By default the redirect links are relative, which might not be so good for SEO"""

    if func.__name__ == "wrapper":
        return func

    if not config.site_url:
        LOG.warning("config.site_url is required for the absolute URLs to work")
        return func

    if not config.use_directory_urls:
        LOG.warning("only cofig.use_directory_urls is supported for the absolute URLs")
        return func

    # Make sure it ends with a /
    site_url = config.site_url.rstrip("/") + "/"

    def wrapper(site_dir, old_path, new_path):

        # Remove the last /index.html part as we want directory mode
        old_path_abs = posixpath.join(site_dir, old_path).rsplit("/", 1)[0]
        resolved_relative = posixpath.normpath(posixpath.join(old_path_abs, new_path))
        new_ending = resolved_relative.replace(site_dir, "", 1)

        # Make sure it ends with a / for directory mode
        new_ending = new_ending.rstrip("/") + "/"

        # site_url ends with / so make sure to remove it here
        new_ending = new_ending.lstrip("/")

        return func(site_dir, old_path, site_url + new_ending)

    return wrapper
