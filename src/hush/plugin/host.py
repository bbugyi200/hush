"""The plugin server is controlled from this module.

Namely, this module is responsible for instantiating a pluggy.PluginManager[1]
object.

[1]: https://pluggy.readthedocs.io/en/stable/api_reference.html#pluggy.PluginManager
"""

from functools import lru_cache as cache

from pluggy import HookimplMarker, HookspecMarker, PluginManager


hookimpl = HookimplMarker("hush")
hookspec = HookspecMarker("hush")


@cache()
def manager() -> PluginManager:
    """Returns the PluginManager responsible for configuring plugins."""
    from . import builtin, specs

    pm = PluginManager("hush")
    pm.add_hookspecs(specs)
    pm.load_setuptools_entrypoints("hush")
    pm.register(builtin)
    return pm
