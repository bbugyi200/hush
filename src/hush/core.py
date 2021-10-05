"""The hush package's catch-all module.

You should only add code to this module when you are unable to find ANY other
module to add it to.
"""


from typing import Iterable, Optional

from . import plugin


def get_secret(key: str, namespace: Iterable[str] = tuple()) -> Optional[str]:
    """Given a ``key``, retrieve a secret.

    Args:
        key: The key that corresponds to the secret we are hoping to retrieve.
        namespace: The namespace that the secret belongs to (e.g. `["db",
          "foobar"]`). How this argument is used is specific to the tool being
          used to store and retrieve secrets (i.e. is specific to each hook
          implementation).
    """
    pm = plugin.manager()
    secret: Optional[str] = pm.hook.get_secret(key=key, namespace=namespace)
    return secret
