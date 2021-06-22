import selenium
from selenium.webdriver import(
  Chrome,
  ChromeOptions,
  Firefox,
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
    scrape_url=(
      cfg['scrape_url']
    ),
  )
  print(cfg)

  # driver = Firefox()
  # driver.get(
  #   url=cfg.scrape_url,
  # )

  # driver.close()

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
    # '--start-maximized',
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
  print(driver.get_window_position())
  print(
    driver.get_window_rect()
  )
  pyautogui.press('enter')
  # elm.send_keys(Keys.SPACE)
  time.sleep(10)
  
  driver.close()

  



if __name__ == '__main__':
  main()