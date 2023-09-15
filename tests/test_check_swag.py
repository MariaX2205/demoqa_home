from pages.swag_labs import SwagLabs
from conftest import browser


def test_icon(browser):
    test_page = SwagLabs(browser)
    test_page.visit()
    assert test_page.exist_icon()


def test_password(browser):
    test_page = SwagLabs(browser)
    test_page.visit()
    assert test_page.find_field(locator='#password')


def test_name(browser):
    test_page = SwagLabs(browser)
    test_page.visit()
    assert test_page.find_field(locator='#user-name')
