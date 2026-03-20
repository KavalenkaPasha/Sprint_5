from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка «Войти в аккаунт» на главной странице
    LOGIN_FROM_MAIN_BUTTON = (By.XPATH, "//button[contains(.,'Войти в аккаунт')]")

    # Ссылка «Личный кабинет» в шапке сайта
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//header//a[@href='/account']")

    # Ссылка «Конструктор» в шапке сайта
    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//header//a[@href='/' and .//p[normalize-space()='Конструктор']]",
    )

    # Логотип Stellar Burgers
    LOGO_BUTTON = (By.XPATH, "//header//a[@href='/' and .//*[name()='svg']]")

    # Кнопка «Оформить заказ» на главной странице после входа
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[contains(.,'Оформить заказ')]")

    # Вкладка «Булки»
    BUNS_TAB = (
        By.XPATH,
        "//span[normalize-space()='Булки']/ancestor::div[contains(@class,'tab')]",
    )

    # Вкладка «Соусы»
    SAUCES_TAB = (
        By.XPATH,
        "//span[normalize-space()='Соусы']/ancestor::div[contains(@class,'tab')]",
    )

    # Вкладка «Начинки»
    FILLINGS_TAB = (
        By.XPATH,
        "//span[normalize-space()='Начинки']/ancestor::div[contains(@class,'tab')]",
    )

    # Часть CSS-класса активной вкладки
    CURRENT_TAB_CLASS_PART = "tab_tab_type_current"


class LoginPageLocators:
    # Заголовок страницы «Вход»
    PAGE_TITLE = (By.XPATH, "//h2[normalize-space()='Вход']")

    # Поле Email в форме входа
    EMAIL_INPUT = (By.XPATH, "//label[contains(.,'Email')]/following-sibling::input")

    # Поле пароля в форме входа
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")

    # Кнопка «Войти» в форме входа
    LOGIN_BUTTON = (By.XPATH, "//button[contains(.,'Войти')]")

    # Ссылка «Зарегистрироваться»
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")

    # Ссылка «Восстановить пароль»
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")


class RegisterPageLocators:
    # Заголовок страницы «Регистрация»
    PAGE_TITLE = (By.XPATH, "//h2[normalize-space()='Регистрация']")

    # Поле «Имя» в форме регистрации
    NAME_INPUT = (By.XPATH, "//label[contains(.,'Имя')]/following-sibling::input")

    # Поле Email в форме регистрации
    EMAIL_INPUT = (By.XPATH, "//label[contains(.,'Email')]/following-sibling::input")

    # Поле пароля в форме регистрации
    PASSWORD_INPUT = (
        By.XPATH,
        "//label[contains(.,'Пароль')]/following-sibling::input",
    )

    # Кнопка «Зарегистрироваться»
    REGISTER_BUTTON = (By.XPATH, "//button[contains(.,'Зарегистрироваться')]")

    # Сообщение об ошибке для некорректного пароля
    PASSWORD_ERROR_TEXT = (
        By.XPATH,
        "//p[contains(@class,'input__error') and normalize-space()='Некорректный пароль']",
    )

    # Ссылка «Войти» на страницах регистрации и восстановления пароля
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")


class ForgotPasswordPageLocators:
    # Заголовок страницы «Восстановление пароля»
    PAGE_TITLE = (By.XPATH, "//h2[normalize-space()='Восстановление пароля']")

    # Поле Email на странице восстановления пароля
    EMAIL_INPUT = (By.XPATH, "//label[contains(.,'Email')]/following-sibling::input")

    # Кнопка «Восстановить»
    RESTORE_BUTTON = (By.XPATH, "//button[contains(.,'Восстановить')]")

    # Ссылка «Войти» на странице восстановления пароля
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")


class AccountPageLocators:
    # Кнопка «Выход» в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space()='Выход']")
