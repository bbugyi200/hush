"""Hooks for the 'pass' tool[1].

[1]: https://www.passwordstore.org
"""

import logging
from typing import Iterable, Optional

from bugyi.lib import shell
from bugyi.lib.result import Err

from ..host import hookimpl


logger = logging.getLogger(__name__)


@hookimpl(specname="get_secret")  # type: ignore[misc]
def get_secret(
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
