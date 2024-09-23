import pytest
from selene import browser
from utils import attach
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--use-selenoid", action="store_true", help="Use Selenoid for tests")


@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    browser.config.base_url = 'https://thecode.media'
    browser.config.window_width = 1600
    browser.config.window_height = 1080
    use_selenoid = request.config.getoption("--use-selenoid")
    if use_selenoid:
        options = Options()
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "122.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        selenoid_login = os.getenv("SELENOID_LOGIN")
        selenoid_pass = os.getenv("SELENOID_PASS")
        selenoid_url = os.getenv("SELENOID_URL")

        options.capabilities.update(selenoid_capabilities)
        driver = webdriver.Remote(
            command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
            options=options)

        browser.config.driver = driver

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    browser.quit()
