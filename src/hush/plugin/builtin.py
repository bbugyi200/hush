"""Internal (i.e. builtin to hush) plugin hook implementations live here.

All plugin hook implementations[1] found in this module will be enabled by
default.

[1]: https://pluggy.readthedocs.io/en/stable/#implementations
"""


import logging
from typing import Iterable, Optional

from bugyi.lib import shell
from bugyi.lib.errors import Err
import pluggy


logger = logging.getLogger(__name__)
hookimpl = pluggy.HookimplMarker("hush")


@hookimpl(specname="get_secret")  # type: ignore[misc]
def pass_get(*, key: str, namespace: Iterable[str] = tuple()) -> Optional[str]:
    if not shell.command_exists("pass"):
        return None

    if namespace:
        key = f"{'/'.join(namespace)}/{key}"

    out_err_result = shell.safe_popen(["pass", "show", key])
    if isinstance(out_err_result, Err):
        error = out_err_result.err()
        logger.debug("Unable to retrieve secret using 'pass' | %r", error)
        return None

    secret, _ = out_err_result.ok()
    return secret
