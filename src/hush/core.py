"""The hush package's catch-all module.

You should only add code to this module when you are unable to find ANY other
module to add it to.
"""


import os
from typing import Iterable, Optional

from . import plugin


def get_secret(
    key: str, namespace: Iterable[str] = tuple(), *, user: str = None
) -> Optional[str]:
    """Given a ``key``, retrieve a secret.

    This function attempts to use every secret-retrieving method registered by
    plugins (internal and external) to obtain the desired secret.

    Args:
        key: The key that corresponds to the secret we are hoping to retrieve.
        namespace: The namespace that the secret belongs to (e.g. `["db",
          "foobar"]`). How this argument is used is specific to the tool being
          used to store and retrieve secrets (i.e. is specific to each hook
          implementation).
        user: If this argument is provided, secret retrieving commands are run
          as ``user`` when possible. This option defaults to the value of the
          HUSH_USER envvar, if defined.

    Returns:
        The secret value returned by the first plugin to successfully retrieve
        the desired secret.
            OR
        None, if none of the registered plugins were able to retrieve the
        desired secret.
    """
    pm = plugin.manager()
    user = user or os.getenv("HUSH_USER")
    secret: Optional[str] = pm.hook.get_secret(
        key=key, namespace=namespace, user=user
    )
    return secret


class Hush:
    """Hush class to constrain context of get_secret() function.

    Can be used as an alternative to calling this module's global
    ``get_secret()`` function directly.
    """

    def __init__(
        self, namespace: Iterable[str] = tuple(), *, user: str = None
    ):
        self._namespace = list(namespace)
        self._user = user

    def get_secret(
        self, key: str, namespace: Iterable[str] = tuple(), *, user: str = None
    ) -> Optional[str]:
        """Given a ``key``, retrive a secret.

        Note:
            * The ``namespace`` argument, if provided, will be used to extend
              the namespace specified when initializing this class.
            * The ``user`` argument, if provided, will override the user
              specified when initializing this class.

        Refer to ``help(hush.get_secret)`` for more information.
        """
        namespace = self._namespace + list(namespace)
        user = user or self._user
        return get_secret(key, namespace=namespace, user=user)
