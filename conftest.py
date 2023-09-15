import pytest
from selenium import webdriver


@pytest.fixture(
    scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver  # это аналог return но не возвращает ничего
    driver.quit()  # функция - это три этих строчки