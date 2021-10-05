"""Internal (i.e. builtin to hush) plugin hook implementations live here.

All plugin hook implementations[1] found in this module will be enabled by
default.

[1]: https://pluggy.readthedocs.io/en/stable/#implementations
"""


import logging
import os
from typing import Iterable, Optional

from bugyi.lib import shell
from bugyi.lib.result import Err
import pluggy


logger = logging.getLogger(__name__)
hookimpl = pluggy.HookimplMarker("hush")


@hookimpl(tryfirst=True, specname="get_secret")  # type: ignore[misc]
def envvar_get(key: str, namespace: Iterable[str]) -> Optional[str]:
    """Implements get_secret() hook by checking for environment variables."""
    key = key.upper()

    if namespace:
        key = f"{'_'.join(part.upper() for part in namespace)}_{key}"

    key = f"HUSH_{key}"

    return os.getenv(key)


@hookimpl(specname="get_secret")  # type: ignore[misc]
def pass_get(
    key: str, namespace: Iterable[str], user: Optional[str]
) -> Optional[str]:
    """Implements get_secret() hook using 'pass'.

    See the tool's official documentation[1] for more information.

    [1]: https://www.passwordstore.org/
    """
    if not shell.command_exists("pass"):
        logger.debug(
            "The 'pass' command does not appear to exist on this machine."
        )
        return None

    if namespace:
        key = f"{'/'.join(namespace)}/{key}"

    cmd_list = []
    if user is not None:
        cmd_list.extend(["sudo", "-u", user])

    cmd_list.extend(["pass", "show", key])

    out_err_result = shell.safe_popen(cmd_list)
    if isinstance(out_err_result, Err):
        error = out_err_result.err()
        logger.debug(
            "Unable to retrieve secret using 'pass': %s", error.report()
        )
        return None

    secret, _ = out_err_result.ok()
    return secret
