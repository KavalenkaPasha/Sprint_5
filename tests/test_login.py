from helpers import register_user, login
from locators import (
    MainPageLocators,
    RegisterPageLocators,
    ForgotPasswordPageLocators,
)
from urls import BASE_URL


def test_login_from_main_button(driver):
    email, password = register_user(driver)

    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.LOGIN_FROM_MAIN_BUTTON).click()
    login(driver, email, password)

    assert driver.find_element(*MainPageLocators.MAKE_ORDER_BUTTON).is_displayed()


def test_login_from_personal_account(driver):
    email, password = register_user(driver)

    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    login(driver, email, password)

    assert driver.find_element(*MainPageLocators.MAKE_ORDER_BUTTON).is_displayed()


def test_login_from_registration_form(driver):
    email, password = register_user(driver)

    driver.get(f"{BASE_URL}register")
    driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
    login(driver, email, password)

    assert driver.find_element(*MainPageLocators.MAKE_ORDER_BUTTON).is_displayed()


def test_login_from_forgot_password_form(driver):
    email, password = register_user(driver)

    driver.get(f"{BASE_URL}forgot-password")
    driver.find_element(*ForgotPasswordPageLocators.LOGIN_LINK).click()
    login(driver, email, password)

    assert driver.find_element(*MainPageLocators.MAKE_ORDER_BUTTON).is_displayed()
