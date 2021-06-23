from __future__ import (
  annotations,
)
import selenium
from selenium.webdriver import(
  Chrome,
  ChromeOptions,
  ActionChains,
)
from webdriver_manager.chrome \
import (
  ChromeDriverManager,
)

from \
  selenium.webdriver \
  .common.by \
import (
  By,
)

from \
  selenium.webdriver \
  .common.keys \
import (
  Keys,
)
import time
import dataclasses
import pyautogui
  

from io import BytesIO
from PIL import (
  Image,
  ImageOps,
)
import base64 
from base64 import (
  b64decode,
)
import pytesseract


def set_globals():
  global cfd, root
  import os
  cfd = os.path.dirname(
    __file__,
  )
  cfd = os.path.abspath(cfd)
  root = f'{cfd}/../'



@dataclasses.dataclass
class SushidaCfg():
  scrape_url: str
  repetitions: int
  interval: float


import typing

class Sushida():
  def __call__(
    self,
  ) -> typing.NoReturn:
    self.__open()
    self.__start()
    self.__play()
    self.__game.screenshot(
      'data/result.png',
    )


  def __init__(
    self,
    cfg: SushidaCfg,
  ) -> typing.NoReturn:
    self.__cfg = cfg
    self.__set_driver()


  def __set_driver(
    self,
  ) -> typing.NoReturn:
    opts = ChromeOptions()
    for opt in [
      '--no-sandbox',
      # '--headless',
      # '--disable-dev-shm-usage',
      # '--start-fullscreen',
      '--start-maximized',
    ]:
      opts.add_argument(opt)
    manager = (
      ChromeDriverManager()
    )
    self.__driver = Chrome(
      manager.install(),
      options=opts,
    )


  def __open(
    self,
  ) -> typing.NoReturn:
    driver = self.__driver
    cfg = self.__cfg
    driver.get(
      url=cfg.scrape_url,
    )
    time.sleep(1)
    driver.find_element(
      by=By.CLASS_NAME,
      value='main_play',
    ).find_elements(
      by=By.TAG_NAME,
      value='a',
    )[0].click()
    time.sleep(6)
    game = driver.find_element(
      by=By.ID,
      value='#canvas',
    )
    self.__game = game


  
  def __start(
    self,
  ) -> typing.NoReturn:
    ActionChains(
      self.__driver,
    ).move_to_element_with_offset(
      self.__game,
      250,
      250,
    ).click().release().perform()
    time.sleep(1)
    act = ActionChains(
      self.__driver,
    ).move_to_element_with_offset(
      self.__game,
      250,
      320,
    ).click().release().perform()
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(3)

  

  def __play(
    self,
  ) -> typing.NoReturn:
    cfg = self.__cfg
    n = cfg.repetitions
    t = cfg.interval
    for i in range(n):
      self.__eat()
      time.sleep(t) 
    time.sleep(
      120 + n * (0.7 - t)
    )

  def __screenshot(
    self,
  ) -> typing.NoReturn:
    bytes_img = b64decode(
      self.__game
      .screenshot_as_base64,
    )
    self.__img = Image.open(
      BytesIO(bytes_img),
    )

  
  def __process_img(
    self,
  ) -> typing.NoReturn:
    ...
    img = self.__img
    w, _ = img.size
    pad = 76   
    img = img.crop((
      pad, 228, w - pad, 256,
    ))
    img = ImageOps.grayscale(img)
    img = img.convert('L')
    img = img.point(
      lut=lambda x: (
        (1 << 8) - 1 
        if x >= 1 << 7 else 0
      ),
    )
    img = ImageOps.invert(img)
    self.__img = img
  

  def __enter__(
    self,
  ) -> Sushida:
    return self


  def __exit__(
    self, 
    exc_type, 
    exc_value, 
    traceback,
  ) -> typing.NoReturn:
    self.__driver.close()
   

  def __ocr(
    self,
  ) -> typing.NoReturn:
    self.__txt = pytesseract.image_to_string(
      self.__img,
      config="-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz!?-,",
    ).strip()

    print(self.__txt)
    

  def __eat(
    self,
  ) -> typing.NoReturn:
    self.__screenshot()
    self.__process_img()
    self.__ocr()
    pyautogui.write(self.__txt)




    
def main():
  set_globals()
  from lib import (
    LoadYml,
  )
  load_yml = LoadYml()
  cfg_path = (
    f'{root}/config.yml'
  )
  cfg = load_yml(cfg_path)
  cfg = SushidaCfg(
    **load_yml(cfg_path),
  )
  with Sushida(cfg) as sushida:
    sushida()


 



if __name__ == '__main__':
  main()