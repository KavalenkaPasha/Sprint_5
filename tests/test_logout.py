from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from generators import generate_email, generate_password
from locators import MainPageLocators, LoginPageLocators, RegisterPageLocators, AccountPageLocators

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


def test_logout_from_account(driver):
    _register_and_login(driver)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_contains('/account'))

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.url_contains('/login'))

    assert '/login' in driver.current_url
