"""Tests for the hush package."""

from pytest_mock.plugin import MockerFixture
from pytest_subprocess.core import FakeProcess

from hush import get_secret


def test_get_secret__PASS(
    mocker: MockerFixture, fake_process: FakeProcess
) -> None:
    """Test the get_secret() function with 'pass'."""
    mocker.patch("bugyi.lib.shell.command_exists", return_value=True)

    expected_secret = "FOOOO"
    fake_process.register_subprocess(
        ["pass", "show", "foo"], stdout=expected_secret
    )
    secret = get_secret("foo")
    assert secret == expected_secret

    expected_secret = "KUNG FOOOOOOO!!!"
    fake_process.register_subprocess(
        ["pass", "show", "path/to/foo"], stdout=expected_secret
    )
    secret = get_secret("foo", namespace=["path", "to"])
    assert secret == expected_secret
