from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver
import time
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en, fr, es, ru etc.")

@pytest.fixture()
def browser(request):
    options = Options()
    language = str(request.config.getoption("--language"))
    if language == "None":
        raise pytest.UsageError("Please, specify the language!")
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    time.sleep(5)
    browser.quit()


