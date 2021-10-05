"""Tests for the hush package."""

from hush import get_secret

from .conftest import FOO, KUNG_FOO


def test_get_secret__PASS(mock_pass: None) -> None:
    """Test the get_secret() function with 'pass'."""
    del mock_pass

    secret = get_secret("foo")
    assert secret == FOO

    secret = get_secret("foo", namespace=["path", "to"])
    assert secret == KUNG_FOO


def test_get_secret__ENVVAR(mock_envvars: None) -> None:
    """Test the get_secret() function with environment variables."""
    del mock_envvars

    secret = get_secret("foo")
    assert secret == FOO
