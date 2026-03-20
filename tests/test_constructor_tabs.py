from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import MainPageLocators

BASE_URL = "https://stellarburgers.education-services.ru/"


def _click(driver, locator, timeout=10):
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    try:
        element.click()
    except Exception:
        driver.execute_script("arguments[0].click();", element)


def _is_current_tab(driver, locator, timeout=10):
    """Проверяет, что вкладка стала активной.

    В интерфейсе класс активной вкладки проставляется не мгновенно (после скролла/анимации),
    поэтому ждём появления нужной части CSS-класса.
    """

    def _tab_has_current_class(_driver):
        el = _driver.find_element(*locator)
        return MainPageLocators.CURRENT_TAB_CLASS_PART in (el.get_attribute("class") or "")

    return WebDriverWait(driver, timeout).until(_tab_has_current_class)


def test_switch_to_sauces_tab(driver):
    driver.get(BASE_URL)
    _click(driver, MainPageLocators.SAUCES_TAB)
    assert _is_current_tab(driver, MainPageLocators.SAUCES_TAB)


def test_switch_to_fillings_tab(driver):
    driver.get(BASE_URL)
    _click(driver, MainPageLocators.FILLINGS_TAB)
    assert _is_current_tab(driver, MainPageLocators.FILLINGS_TAB)


def test_switch_to_buns_tab(driver):
    driver.get(BASE_URL)
    _click(driver, MainPageLocators.SAUCES_TAB)
    _click(driver, MainPageLocators.BUNS_TAB)
    assert _is_current_tab(driver, MainPageLocators.BUNS_TAB)
