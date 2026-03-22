from helpers import click_element, is_current_tab
from locators import MainPageLocators
from urls import BASE_URL


def test_switch_to_sauces_tab(driver):
    driver.get(BASE_URL)
    click_element(driver, MainPageLocators.SAUCES_TAB)
    assert is_current_tab(driver, MainPageLocators.SAUCES_TAB)


def test_switch_to_fillings_tab(driver):
    driver.get(BASE_URL)
    click_element(driver, MainPageLocators.FILLINGS_TAB)
    assert is_current_tab(driver, MainPageLocators.FILLINGS_TAB)


def test_switch_to_buns_tab(driver):
    driver.get(BASE_URL)
    click_element(driver, MainPageLocators.SAUCES_TAB)
    click_element(driver, MainPageLocators.BUNS_TAB)
    assert is_current_tab(driver, MainPageLocators.BUNS_TAB)
