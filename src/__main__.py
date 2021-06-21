import selenium
from selenium.webdriver import(
  Firefox,
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

  driver = Firefox()
  driver.get(
    url=cfg.scrape_url,
  )

  # driver.close()


if __name__ == '__main__':
  main()