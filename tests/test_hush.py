"""Tests for the hush package."""

from hush import Hush, get_secret

from .conftest import FOO


def test_get_secret__PASS(mock_pass: None) -> None:
    """Test the get_secret() function with 'pass'."""
    del mock_pass

    secret = get_secret("foo")
    assert secret == FOO

    namespace = ["path", "to"]
    secret = get_secret("foo", namespace=namespace)
    assert secret == FOO

    hush = Hush(namespace=namespace)
    secret = hush.get_secret("foo")
    assert secret == FOO


def test_get_secret__ENVVAR(mock_envvars: None) -> None:
    """Test the get_secret() function with environment variables."""
    del mock_envvars

    secret = get_secret("foo")
    assert secret == FOO
