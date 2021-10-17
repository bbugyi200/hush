"""Internal (i.e. builtin to hush) plugin hook implementations live here.

All plugin hook implementations[1] found in this package will be enabled by
default.

[1]: https://pluggy.readthedocs.io/en/stable/#implementations
"""

from ._core import get_plugin_modules


__all__ = ["get_plugin_modules"]
