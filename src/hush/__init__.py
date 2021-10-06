"""A Python library that helps manage secrets.

Uses the secret management tools (e.g. pass) specified by (internal and
external) plugin hooks.
"""

import logging as _logging

from .core import Hush, get_secret


__author__ = "Bryan M Bugyi"
__email__ = "bryanbugyi34@gmail.com"
__version__ = "0.3.0"

_logging.getLogger(__name__).addHandler(_logging.NullHandler())
