import random
import string

# В задании указан формат email для регистрации:
# имя_фамилия_номер_когорты_любые 3 цифры@домен
# Чтобы не получить коллизии в рамках одного прогона тестов —
# следим, чтобы 3-значный суффикс не повторялся.
_USED_SUFFIXES: set[int] = set()


def generate_email(
    name: str = "pavel",
    surname: str = "kavalenka",
    cohort: int | str = 42,
    domain: str = "yandex.ru",
) -> str:
    """Генерирует уникальный email строго в формате из задания."""
    name = (name or "test").strip().lower()
    surname = (surname or "test").strip().lower()

    while True:
        suffix = random.randint(0, 999)
        if suffix not in _USED_SUFFIXES:
            _USED_SUFFIXES.add(suffix)
            break

    return f"{name}_{surname}_{cohort}_{suffix:03d}@{domain}"


def generate_password(length: int = 10) -> str:
    """Генерирует пароль длиной не меньше 6 символов."""
    length = max(length, 6)
    alphabet = string.ascii_letters + string.digits
    return "".join(random.choice(alphabet) for _ in range(length))
