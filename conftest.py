import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    WebDriverWait(driver, 10)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
