import dataclasses

import selenium.webdriver
import selenium.webdriver.remote.webdriver
import webdriver_manager.chrome


@dataclasses.dataclass(frozen=True)
class ChromeOptions:
    no_sandbox: bool = True
    start_maximized: bool = True


def create_chrome_driver(
    headless: bool = False,
) -> selenium.webdriver.remote.webdriver.WebDriver:
    options = selenium.webdriver.ChromeOptions()
    for opt in [
        "--no-sandbox",
        "--start-maximized",
    ]:
        options.add_argument(opt)
        # all https://peter.sh/experiments/chromium-command-line-switches/
    options.headless = headless
    manager = webdriver_manager.chrome.ChromeDriverManager()
    return selenium.webdriver.Chrome(
        options=options,
        executable_path=manager.install(),
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
