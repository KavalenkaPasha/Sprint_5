from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from generators import generate_email, generate_password
from locators import MainPageLocators, LoginPageLocators, RegisterPageLocators

BASE_URL = 'https://stellarburgers.education-services.ru/'


def _register_and_login(driver):
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

    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.LOGIN_FROM_MAIN_BUTTON).click()
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.MAKE_ORDER_BUTTON))


def test_go_to_account_by_header_click(driver):
    _register_and_login(driver)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_contains('/account'))

    assert '/account' in driver.current_url


def test_from_account_to_constructor_by_constructor_link(driver):
    _register_and_login(driver)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_contains('/account'))

    driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))

    assert driver.current_url == BASE_URL


def test_from_account_to_constructor_by_logo(driver):
    _register_and_login(driver)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_contains('/account'))

    driver.find_element(*MainPageLocators.LOGO_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))

    assert driver.current_url == BASE_URL
