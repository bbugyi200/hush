"""This file contains shared fixtures and pytest hooks.

https://docs.pytest.org/en/6.2.x/fixture.html#conftest-py-sharing-fixtures-across-multiple-files
"""

from _pytest.nodes import Item
from typeguard import typechecked


def pytest_runtest_call(item: Item) -> None:
    """Called once for each test function.

    See the following URL for more information on this pytest hook:
        https://docs.pytest.org/en/6.2.x/reference.html#pytest.hookspec.pytest_runtest_call
    """
    # Decorate every test function [e.g. test_foo()] with typeguard's
    # typechecked() decorator.
    test_func = getattr(item, "obj", None)
    if test_func is not None:
        setattr(item, "obj", typechecked(test_func))
