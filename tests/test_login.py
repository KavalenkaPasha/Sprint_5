from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from generators import generate_email, generate_password
from locators import (
    MainPageLocators,
    LoginPageLocators,
    RegisterPageLocators,
    ForgotPasswordPageLocators,
)

BASE_URL = 'https://stellarburgers.education-services.ru/'


def _register_user(driver):
    email = generate_email()
    password = generate_password()

    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.LOGIN_FROM_MAIN_BUTTON).click()
    driver.find_element(*LoginPageLocators.REGISTER_LINK).click()

    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys('Pavel')
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.PAGE_TITLE))
    return email, password


def _login(driver, email, password):
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.MAKE_ORDER_BUTTON))


def test_login_from_main_button(driver):
    email, password = _register_user(driver)

    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.LOGIN_FROM_MAIN_BUTTON).click()
    _login(driver, email, password)

    assert driver.find_element(*MainPageLocators.MAKE_ORDER_BUTTON).is_displayed()


def test_login_from_personal_account(driver):
    email, password = _register_user(driver)

    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    _login(driver, email, password)

    assert driver.find_element(*MainPageLocators.MAKE_ORDER_BUTTON).is_displayed()


def test_login_from_registration_form(driver):
    email, password = _register_user(driver)

    driver.get(f'{BASE_URL}register')
    driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
    _login(driver, email, password)

    assert driver.find_element(*MainPageLocators.MAKE_ORDER_BUTTON).is_displayed()


def test_login_from_forgot_password_form(driver):
    email, password = _register_user(driver)

    driver.get(f'{BASE_URL}forgot-password')
    driver.find_element(*ForgotPasswordPageLocators.LOGIN_LINK).click()
    _login(driver, email, password)

    assert driver.find_element(*MainPageLocators.MAKE_ORDER_BUTTON).is_displayed()
