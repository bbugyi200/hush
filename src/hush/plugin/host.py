"""The plugin server is controlled from this module.

Namely, this module is responsible for instantiating a pluggy.PluginManager[1]
object.

[1]: https://pluggy.readthedocs.io/en/stable/api_reference.html#pluggy.PluginManager
"""

from functools import lru_cache as cache

from pluggy import PluginManager


@cache  # type: ignore[arg-type]
def manager() -> PluginManager:
    """Returns the PluginManager responsible for configuring plugins."""
    result = PluginManager("hush")
    return result
