import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def open_webpage(request):
    driver = webdriver.Chrome()
    driver.get("https://boxberry.ru/")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()
