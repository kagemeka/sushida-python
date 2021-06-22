import selenium
from selenium.webdriver import(
  Chrome,
  ChromeOptions,
  ActionChains,
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
import requests

import dataclasses


def set_globals():
  global cfd, root
  import os
  cfd = os.path.dirname(
    __file__,
  )
  cfd = os.path.abspath(cfd)
  root = f'{cfd}/../'



@dataclasses.dataclass
class Cfg():
  scrape_url: str
  

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
  cfg = Cfg(
    **load_yml(cfg_path),
  )

  from webdriver_manager.chrome \
  import (
    ChromeDriverManager,
  )

  options = ChromeOptions()
  opts = [
    '--no-sandbox',
    # '--headless',
    # '--disable-dev-shm-usage',
    # '--start-fullscreen',
    '--start-maximized',
  ]
  

  for x in opts:
    options.add_argument(x)


  manager = ChromeDriverManager()

  driver = Chrome(
    manager.install(),
    options=options,
  )
  driver.get(
    url=cfg.scrape_url,
  )
  time.sleep(1)
  elm = driver.find_element(
    by=By.CLASS_NAME,
    value='main_play',
  )
  elms = elm.find_elements(
    by=By.TAG_NAME,
    value='a',
  )
  elms[0].click()
  
  time.sleep(1 << 3)
  elm = driver.find_element(
    by=By.ID,
    value='#canvas',
  )

  act = ActionChains(
    driver,
  ).move_to_element_with_offset(
    elm,
    250,
    250,
  ).click().release()
  act.perform()
  time.sleep(1)

  act = ActionChains(
    driver,
  ).move_to_element_with_offset(
    elm,
    250,
    320,
  ).click().release()
  act.perform()
  time.sleep(1)
  import pyautogui
  pyautogui.press('space')
  time.sleep(3)
  from io import BytesIO
  from PIL import (
    Image,
    ImageOps,
  )
  import base64 
  import pytesseract

  for i in range(180):
    b64_img = (
      elm.screenshot_as_base64
    )
    bytes_img = base64.b64decode(
      b64_img,
    )
    img = Image.open(
      BytesIO(bytes_img),
    )
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
    txt = pytesseract.image_to_string(
      img,
      config="-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz!?-,",
    ).strip()

    print(txt)
    
    pyautogui.write(txt)
    time.sleep(0.1)

  time.sleep(180)
  elm.screenshot(
    'data/result.png',
  )
  driver.close()

  



if __name__ == '__main__':
  main()