"""Small MkDocs hook, to allow to change the logo in the Social Plugin

MIT Licence 2024 Kamil Krzyśków (HRY) for Fiori Tracker (fioritracker.org)
"""

import inspect
import logging
from copy import deepcopy

from mkdocs.plugins import PrefixedLogger, event_priority

HOOK_NAME = "change_social_logo"
LOG: PrefixedLogger = PrefixedLogger(HOOK_NAME, logging.getLogger(f"mkdocs.hooks.{HOOK_NAME}"))


@event_priority(100)
def on_config(config):

    from material.plugins.social.plugin import SocialPlugin

    # Skip if applied in mkdocs serev
    if SocialPlugin._load_logo.__name__ == "wrapper":
        return

    signature = "(self, config)"

    if str(inspect.signature(SocialPlugin._load_logo)) != signature:
        LOG.warning("function signature changed")
        return

    SocialPlugin._load_logo = load_logo_wrapper(SocialPlugin._load_logo, config.theme)


def load_logo_wrapper(func, theme):

    if func.__name__ == "wrapper":
        return func

    class DummyConfig: ...

    theme = deepcopy(theme)

    def wrapper(self, config):
        cfg = DummyConfig()
        cfg.theme = theme
        cfg.docs_dir = config.docs_dir
        cfg.theme["logo"] = "assets/images/social_logo.png"

        return func(self, cfg)

    return wrapper
