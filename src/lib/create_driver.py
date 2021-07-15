from selenium.webdriver import(
  Chrome,
  ChromeOptions,
)
from webdriver_manager.chrome \
import (
  ChromeDriverManager,
)
from \
  selenium.webdriver.remote \
  .webdriver \
import (
  WebDriver,
)


def create_driver(
  headless: bool = False,
) -> WebDriver:
  opts = ChromeOptions()
  for opt in [
    '--no-sandbox',
    '--start-maximized',
  ]:
    opts.add_argument(opt)
  opts.headless = headless
  manager = (
    ChromeDriverManager()
  )
  return Chrome(
    manager.install(),
    options=opts,
  )

