"""The hush.plugin.builtin package's catch-all module.

You should only add code to this module when you are unable to find ANY other
module to add it to.
"""

import importlib
import logging
from pathlib import Path
from types import ModuleType
from typing import List


logger = logging.getLogger(__name__)


def get_plugin_modules() -> List[ModuleType]:
    """Returns a list of all the modules in this directory.

    Note:
        This module and any other module whose name starts with an underscore
        will not be included in the returned result.
    """
    result = []
    for mod_path in Path(__file__).resolve().parent.glob("*.py"):
        mod_name = mod_path.stem
        if mod_name.startswith("_"):
            logger.debug("Skipping this module: %r", mod_name)
            continue

        mod = importlib.import_module("." + mod_name, package=__package__)
        logger.debug("Found plugin module for %r: %r", mod_name, mod)
        result.append(mod)

    return result
