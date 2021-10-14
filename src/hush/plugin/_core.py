"""The hush.plugin package's catch-all module.

You should only add code to this module when you are unable to find ANY other
module to add it to.
"""

from functools import lru_cache as cache

from pluggy import PluginManager

from . import _builtin, _specs


@cache()
def manager() -> PluginManager:
    """Returns the PluginManager[1] responsible for configuring plugins.

    [1]: https://pluggy.readthedocs.io/en/stable/api_reference.html#pluggy.PluginManager
    """
    pm = PluginManager("hush")
    pm.add_hookspecs(_specs)
    pm.load_setuptools_entrypoints("hush")

    for mod in _builtin.get_plugin_modules():
        pm.register(mod)

    return pm
