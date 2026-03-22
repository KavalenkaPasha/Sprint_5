from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import register_and_login
from locators import MainPageLocators
from urls import BASE_URL


def test_go_to_account_by_header_click(driver):
    register_and_login(driver)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    assert WebDriverWait(driver, 10).until(EC.url_contains("/account"))


def test_from_account_to_constructor_by_constructor_link(driver):
    register_and_login(driver)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_contains("/account"))

    driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

    assert WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))


def test_from_account_to_constructor_by_logo(driver):
    register_and_login(driver)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_contains("/account"))

    driver.find_element(*MainPageLocators.LOGO_BUTTON).click()

    assert WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
