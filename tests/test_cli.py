"""End-to-end tests using the 'hush' executable."""

from typing import Sequence

from _pytest.capture import CaptureFixture
from pytest import mark

from hush.cli import main

from .conftest import FOO


params = mark.parametrize
cli_params = params(
    "args,expected",
    [
        (["foo"], FOO),
        (["foo", "-n", "path,to"], FOO),
    ],
)


@cli_params
def test_pass(
    capsys: CaptureFixture,
    mock_pass: None,
    args: Sequence[str],
    expected: str,
) -> None:
    """Tests that 'hush' can retrieve secrets from 'pass'."""
    del mock_pass

    args = list(args)
    main([""] + args)

    captured = capsys.readouterr()
    actual = captured.out.strip()
    assert actual == expected


@cli_params
def test_envvars(
    capsys: CaptureFixture,
    mock_envvars: None,
    args: Sequence[str],
    expected: str,
) -> None:
    """Tests that 'hush' can retrieve secrets from environment variables."""
    del mock_envvars

    args = list(args)
    main([""] + args)

    captured = capsys.readouterr()
    actual = captured.out.strip()
    assert actual == expected
