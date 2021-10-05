"""Contains the hush package's main entry point."""

from typing import List, Sequence

import clap
from logutils import Logger
from pydantic.dataclasses import dataclass

from . import __doc__ as DESCRIPTION, get_secret


@dataclass(frozen=True)
class Arguments(clap.Arguments):
    """Command-line arguments."""

    key: str
    namespace: List[str]


def parse_cli_args(argv: Sequence[str]) -> Arguments:
    """Parses command-line arguments."""
    parser = clap.Parser(name="hush", description=DESCRIPTION)
    parser.add_argument(
        "key",
        help=(
            "The key that corresponds with the secret that we wish to"
            " retrieve."
        ),
    )
    parser.add_argument(
        "-n",
        "--namespace",
        type=lambda x: x.split(","),
        default=[],
        help=(
            "The namespace the secret is apart of. This argument should be a"
            " comma-separated list of namespace parts."
        ),
    )

    args = parser.parse_args(argv[1:])
    kwargs = vars(args)

    return Arguments(**kwargs)


def run(args: Arguments) -> int:
    """This function acts as this tool's main entry point."""
    log = Logger(__name__).bind_fargs(locals())

    secret = get_secret(args.key, namespace=args.namespace)
    if secret is None:
        log.error(
            "Hush was unable to retrieve this secret.",
            key=args.key,
            namespace=args.namespace,
        )
        return 1

    print(secret)
    return 0


main = clap.main_factory(parse_cli_args, run)
