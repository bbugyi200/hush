"""Plugin package.

This package sets up a plugin architecture using pluggy.

See pluggy's documentation[1] for more information.

[1]: https://pluggy.readthedocs.io/en/stable
"""

from .builtin import hookimpl
from .host import manager
