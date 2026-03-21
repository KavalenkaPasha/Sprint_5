from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from generators import generate_email, generate_password
from locators import MainPageLocators, LoginPageLocators, RegisterPageLocators
from urls import BASE_URL


def test_successful_registration(driver):
    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.LOGIN_FROM_MAIN_BUTTON).click()
    driver.find_element(*LoginPageLocators.REGISTER_LINK).click()

    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Pavel")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(
        generate_password()
    )
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    assert WebDriverWait(driver, 10).until(EC.url_contains("/login"))


def test_registration_invalid_password_error(driver):
    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.LOGIN_FROM_MAIN_BUTTON).click()
    driver.find_element(*LoginPageLocators.REGISTER_LINK).click()

    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Pavel")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys("12345")
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR_TEXT)
    )
