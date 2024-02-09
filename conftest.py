import pytest
from selene import browser


@pytest.fixture(scope='function')
def set_window_size():
    browser.config.window_height = 800
    browser.config.window_width = 800


@pytest.fixture(scope='function')
def open_browser(set_window_size):
    browser.open('https://google.com')

