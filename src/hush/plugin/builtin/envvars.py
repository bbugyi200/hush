"""Environment variable hooks."""

import logging
import os
from typing import Iterable, Optional

from ..host import hookimpl


logger = logging.getLogger(__name__)


@hookimpl(tryfirst=True, specname="get_secret")  # type: ignore[misc]
def get_secret(key: str, namespace: Iterable[str]) -> Optional[str]:
    """Implements get_secret() hook by checking for environment variables."""
    key = key.upper()

    if namespace:
        prefix = "_".join(part.replace(".", "_").upper() for part in namespace)
        key = f"{prefix}_{key}"

    key = f"HUSH_{key}"

    result = os.getenv(key)
    if result is None:
        logger.debug("No environment variable named %s is defined.", key)

    return result
