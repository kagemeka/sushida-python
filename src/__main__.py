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
  from lib import (
    LoadYml,
    Sushida,
    SushidaCfg,
  )
  load_yml = LoadYml()
  cfg_path = (
    f'{root}/config.yml'
  )
  cfg = load_yml(cfg_path)
  cfg['data_dir'] = (
    f'{root}/data/'
  )
  cfg = SushidaCfg(**cfg)
  with Sushida(cfg) as sushida:
    sushida()


if __name__ == '__main__':
  main()