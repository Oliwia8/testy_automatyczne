import pytest as pytest
from pages.base_page_objects import BasePageObject
from playwright.sync_api import sync_playwright
from pages.buttons_page_objects import ButtonsPageObjects
from pages.text_box_page_objects import TextBoxPageObjects


@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()


@pytest.fixture
def base_page_object(browser):
    return BasePageObject(browser)


@pytest.fixture
def buttons_page_objects(browser):
    return ButtonsPageObjects(browser)


@pytest.fixture
def text_box_page_objects(browser):
    return TextBoxPageObjects(browser)
