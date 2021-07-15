from kgmk.yml import (
  Load as LoadYml,
)
from kgmk.sushida import (
  Sushida,
  SushidaCfg,
)
from lib import (
  create_driver,
)


def set_globals():
  global cfd, root
  import os
  cfd = os.path.dirname(
    __file__,
  )
  cfd = os.path.abspath(cfd)
  root = f'{cfd}/../'

    
def main():
  set_globals()
  load_yml = LoadYml()
  cfg_path = (
    f'{root}/config.yml'
  )
  cfg = load_yml(cfg_path)
  sushida_cfg = SushidaCfg(
    **cfg['sushida'],
    result_path=(
      f'{root}data/result.png'
    ),
  )
  print(cfg)
  driver = create_driver(
    cfg[
      'webdriver'
    ][
      'headless'
    ],
  )
  sushida = Sushida(
    sushida_cfg,
  )
  sushida(driver)


if __name__ == '__main__':
  main()