"""
Все вспомогательные функции вынесены сюда, чтобы файлы с тестами
содержали только сами тест-функции.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from generators import generate_email, generate_password
from locators import (
    MainPageLocators,
    LoginPageLocators,
    RegisterPageLocators,
)
from urls import BASE_URL


# ---------------------------------------------------------------------------
# Навигация по вкладкам конструктора
# ---------------------------------------------------------------------------

def click_element(driver, locator, timeout=10):
    """Ждёт кликабельности элемента, скроллит к нему и кликает."""
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    try:
        element.click()
    except Exception:
        driver.execute_script("arguments[0].click();", element)


def is_current_tab(driver, locator, timeout=10):
    """Ждёт, пока вкладка не получит CSS-класс активной, и возвращает True.

    Класс активной вкладки проставляется не мгновенно (после скролла/анимации),
    поэтому используем явное ожидание вместо мгновенной проверки.
    """

    def _tab_has_current_class(_driver):
        el = _driver.find_element(*locator)
        return MainPageLocators.CURRENT_TAB_CLASS_PART in (
            el.get_attribute("class") or ""
        )

    return WebDriverWait(driver, timeout).until(_tab_has_current_class)


# ---------------------------------------------------------------------------
# Регистрация и вход
# ---------------------------------------------------------------------------

def register_user(driver):
    """Регистрирует нового пользователя и возвращает (email, password)."""
    email = generate_email()
    password = generate_password()

    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.LOGIN_FROM_MAIN_BUTTON).click()
    driver.find_element(*LoginPageLocators.REGISTER_LINK).click()

    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Pavel")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.PAGE_TITLE)
    )
    return email, password


def login(driver, email, password):
    """Вводит учётные данные и нажимает «Войти»."""
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.MAKE_ORDER_BUTTON)
    )


def register_and_login(driver):
    """Регистрирует пользователя и сразу выполняет вход."""
    email, password = register_user(driver)

    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.LOGIN_FROM_MAIN_BUTTON).click()
    login(driver, email, password)
