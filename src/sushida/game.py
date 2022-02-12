from __future__ import annotations

import dataclasses
import logging
import time

import filesystem.path
import PIL
import PIL.Image
import PIL.PngImagePlugin
import pyautogui

# it's needed to import pyautogui to use PIL but the reason is not clear.
import selenium.webdriver
import selenium.webdriver.remote.webdriver
import selenium.webdriver.remote.webelement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import sushida._constants
import sushida._image_processing
import sushida.webdriver

_LOGGER = logging.getLogger(__name__)
_ACTION_MINIMUM_INVERVAL = 1


_GAME_URL = f"{sushida._constants._SITE_URL}/play.html"


@dataclasses.dataclass
class Option:
    soundless: bool = False
    kana: bool = False
    bold: bool = False


def _option_to_url_string(option: Option) -> str:
    return "&".join(
        [opt for opt, enabled in dataclasses.asdict(option).items() if enabled]
    )


def _open(
    driver: selenium.webdriver.remote.webdriver.WebDriver,
    game_option: Option | None = None,
) -> selenium.webdriver.remote.webelement.WebElement:
    WAIT_SEC_AFTER_OPEN = 7
    url = _GAME_URL
    if game_option is not None:
        url += f"?{_option_to_url_string(game_option)}"
    driver.get(url)
    _LOGGER.info("access game page.")
    _LOGGER.info(f"loading game, wait {WAIT_SEC_AFTER_OPEN} sec.")
    time.sleep(WAIT_SEC_AFTER_OPEN)
    _LOGGER.info("game page loaded.")
    game = driver.find_element(by=By.ID, value="#canvas")
    return game


@dataclasses.dataclass(frozen=True)
class _Offset:
    x: int
    y: int


def _start(
    driver: selenium.webdriver.remote.webdriver.WebDriver,
    game: selenium.webdriver.remote.webelement.WebElement,
) -> None:
    START_BUTTON_OFFSET = _Offset(250, 250)
    HIGH_RANK_BUTTON_OFFSET = _Offset(250, 320)
    WAIT_SEC_AFTER_START = 3
    selenium.webdriver.ActionChains(driver).move_to_element_with_offset(
        game,
        START_BUTTON_OFFSET.x,
        START_BUTTON_OFFSET.y,
    ).click().release().perform()
    time.sleep(_ACTION_MINIMUM_INVERVAL)
    selenium.webdriver.ActionChains(driver).move_to_element_with_offset(
        game,
        HIGH_RANK_BUTTON_OFFSET.x,
        HIGH_RANK_BUTTON_OFFSET.y,
    ).click().release().perform()
    time.sleep(_ACTION_MINIMUM_INVERVAL)
    selenium.webdriver.ActionChains(driver).send_keys(Keys.SPACE).perform()
    time.sleep(WAIT_SEC_AFTER_START)


def _take_screenshot(
    game: selenium.webdriver.remote.webelement.WebElement,
) -> PIL.PngImagePlugin.PngImageFile:
    import base64
    import io

    bytes_image = base64.b64decode(game.screenshot_as_base64)

    return PIL.Image.open(io.BytesIO(bytes_image))


@dataclasses.dataclass(frozen=True)
class PlayConfig:
    epochs: int = 150
    interval: float = 1


def _play(
    config: PlayConfig,
    driver: selenium.webdriver.remote.webdriver.WebDriver,
    game: selenium.webdriver.remote.webelement.WebElement,
) -> None:
    # WAIT_TIME_UNTIL_FINISH = 120 + config.epochs * (0.7 - config.interval)
    WAIT_TIME_UNTIL_FINISH = 10
    actions = selenium.webdriver.ActionChains(driver)
    for i in range(config.epochs):
        image = _take_screenshot(game)
        image = sushida._image_processing._preprocess(image)
        text = sushida._image_processing._optical_character_recognition(image)
        actions.send_keys_to_element(game, text).perform()
        # pyautogui.write(text)
        time.sleep(config.interval)
    time.sleep(WAIT_TIME_UNTIL_FINISH)


def _save_result(
    game: selenium.webdriver.remote.webelement.WebElement,
    savepath: str,
) -> None:
    filesystem.path.prepare_directory(savepath)
    game.screenshot(savepath)


def run(
    driver: selenium.webdriver.remote.webdriver.WebDriver,
    game_option: Option | None = None,
    play_config: PlayConfig | None = None,
    result_save_path: str | None = None,
) -> None:
    if play_config is None:
        play_config = PlayConfig()
    game = _open(driver, game_option)
    _start(driver, game)
    _play(play_config, driver, game)
    if result_save_path is not None:
        _save_result(game, result_save_path)
        _LOGGER.info(f'saving result to "{result_save_path}"')


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
