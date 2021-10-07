"""Internal (i.e. builtin to hush) plugin hook implementations live here.

All plugin hook implementations[1] found in this package will be enabled by
default.

[1]: https://pluggy.readthedocs.io/en/stable/#implementations
"""

# These hooks must be imported into this package's global namespace so this
# package can be registered as a plugin via `PluginManager.register(builtins)`.
from .envvars import get_secret as _envvars_get_secret
from .pass_store import get_secret as _pass_store_get_secret
