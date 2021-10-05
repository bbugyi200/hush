"""Tests for the hush package."""

import os
from unittest.mock import patch

from pytest_mock.plugin import MockerFixture
from pytest_subprocess.core import FakeProcess

from hush import get_secret


FOO = "FOOOO"
KUNG_FOO = "Kung FOOOOOO!!!"


def test_get_secret__PASS(
    mocker: MockerFixture, fake_process: FakeProcess
) -> None:
    """Test the get_secret() function with 'pass'."""
    mocker.patch("bugyi.lib.shell.command_exists", return_value=True)

    fake_process.register_subprocess(["pass", "show", "foo"], stdout=FOO)
    secret = get_secret("foo")
    assert secret == FOO

    fake_process.register_subprocess(
        ["pass", "show", "path/to/foo"], stdout=KUNG_FOO
    )
    secret = get_secret("foo", namespace=["path", "to"])
    assert secret == KUNG_FOO


@patch.dict(os.environ, {"HUSH_FOO": FOO, "HUSH_PATH_TO_FOO": KUNG_FOO})
def test_get_secret__ENVVAR() -> None:
    """Test the get_secret() function with environment variables."""
    secret = get_secret("foo")
    assert secret == FOO
