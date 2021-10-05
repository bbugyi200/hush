"""This file contains shared fixtures and pytest hooks.

https://docs.pytest.org/en/6.2.x/fixture.html#conftest-py-sharing-fixtures-across-multiple-files
"""

import os
from typing import Iterator
from unittest.mock import patch

from _pytest.nodes import Item
import logutils
from pytest import fixture
from pytest_mock.plugin import MockerFixture
from typeguard import typechecked


FOO = "FOOOO"


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


@fixture(autouse=True, scope="session")
def init_logging() -> None:
    """Initialize logging."""
    logutils.init_logging()


@fixture
def mock_pass(mocker: MockerFixture) -> None:
    """Mocks needed to test 'pass' secrets.

    Mocks subprocess.Popen() so 'pass' appears to exist and contain desired
    secrets.
    """
    mocker.patch("bugyi.lib.shell.command_exists", return_value=True)

    proc_mock = mocker.MagicMock()
    proc_mock.returncode = 0

    popen_mock = mocker.MagicMock(return_value=proc_mock)

    mock_communicate = mocker.MagicMock(return_value=(FOO.encode(), b""))
    proc_mock.communicate = mock_communicate

    mocker.patch("bugyi.lib.shell.sp.Popen", popen_mock)


@fixture
def mock_envvars() -> Iterator[None]:
    """Mocks needed to test environment variable secrets."""
    with patch.dict(os.environ, {"HUSH_FOO": FOO, "HUSH_PATH_TO_FOO": FOO}):
        yield
