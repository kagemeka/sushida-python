from __future__ import annotations

import argparse
import logging
import sys
import typing

import sushida
import sushida.game
import sushida.webdriver

_LOGGING_FORMAT = "%(asctime)s %(levelname)s %(pathname)s %(message)s"
logging.basicConfig(
    format=_LOGGING_FORMAT,
    datefmt="%Y-%m-%d %H:%M:%S%z",
    handlers=[logging.StreamHandler()],
    level=logging.INFO,
)


def run(
    headless: bool = False,
    result_save_path: str | None = None,
) -> None:
    with sushida.webdriver.create_chrome_driver(headless=headless) as driver:
        sushida.game.run(driver, result_save_path=result_save_path)


def _add_run_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--headless",
        action="store_true",
        default=False,
        required=False,
        help="run in headless mode",
    )
    parser.add_argument(
        "-s",
        "--result-save-path",
        dest="result_save_path",
        type=str,
        required=False,
        default=None,
        help="save result image to specified path",
    )


def main(argv: typing.Sequence[str] | None = None) -> None:
    argv = argv if argv is not None else sys.argv[1:]
    parser = argparse.ArgumentParser(prog="sushida")

    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {sushida.__version__}",
    )

    subpersers = parser.add_subparsers(dest="subcommand")
    sub_run = subpersers.add_parser("run", help="play sushida.")
    _add_run_options(sub_run)

    args = parser.parse_args(argv)

    if args.subcommand == "run":
        run(args.headless, args.result_save_path)
    else:
        parser.print_help()

    args = parser.parse_args(argv)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
