import os

import pytest

import sushida.game
import sushida.webdriver


@pytest.mark.skip(reason="cannot use DISPLAY on actions.")
def test_run() -> None:
    save_path = "/tmp/result.png"
    if os.path.exists(save_path):
        os.remove(save_path)
    with sushida.webdriver.create_chrome_driver(headless=True) as driver:
        sushida.game.run(driver, result_save_path=save_path)
    assert os.path.exists(save_path)
