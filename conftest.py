import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    driver = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        service = Service(ChromeDriverManager().install())
        options = Options()
        prefs = {
            "download.default_directory": f"{os.getcwd()}",
            "safebrowsing.enabled": True
        }
        # options.add_argument('--headless=new')
        options.add_experimental_option("prefs", prefs)
        options.add_argument('--disable-gpu')

        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print("\nquit browser..")
    driver.quit()