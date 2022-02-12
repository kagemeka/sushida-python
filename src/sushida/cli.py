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


def run() -> None:
    with sushida.webdriver.create_chrome_driver(headless=True) as driver:
        sushida.game.run(driver, result_save_path="result.png")


def _add_run_options(parse: argparse.ArgumentParser) -> None:
    ...


def main(argv: typing.Sequence[str] | None = None) -> None:
    argv = argv if argv is not None else sys.argv[1:]
    parser = argparse.ArgumentParser(prog="sushida")

    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {sushida.__version__}",
    )

    # args = parser.parse_args(argv)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
