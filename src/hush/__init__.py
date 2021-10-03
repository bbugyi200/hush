"""A Python library that helps manage secrets using tools specified by plugin hooks."""

import logging as _logging

from .hush import dummy


__author__ = "Bryan M Bugyi"
__email__ = "bryanbugyi34@gmail.com"
__version__ = "0.0.1"

_logging.getLogger(__name__).addHandler(_logging.NullHandler())
