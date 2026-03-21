from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import register_and_login
from locators import MainPageLocators, AccountPageLocators


def test_logout_from_account(driver):
    register_and_login(driver)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_contains("/account"))

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)
    ).click()

    assert WebDriverWait(driver, 10).until(EC.url_contains("/login"))
