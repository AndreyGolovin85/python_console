def check_pin(pin: str):
    """Фукция проверяет крректность пин-кода"""
    if 4 < len(pin) < 4 or pin == "1234" or pin.count(pin[0]) == 4:
        return False
    else:
        return True


def check_pass(string: str) -> bool:
    """Функция проверяет пароль."""
    if len(string) < 8 or string.isdigit() or string.isalpha() or not string.isalnum():
        return False
    else:
        return True


def check_name(string: str) -> str:
    """
    Функция проверяет Имена.
    :param string:
    :return:
    """
    list_letters = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м",
                    "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", " "]

    for let in string.lower():
        if let not in list_letters:
            return False
    return True


def check_mail(string: str) -> bool:
    """
    Функция проверяет электроную почту.
    :param string:
    :return:
    """
    return bool("@" in string and "." in string)
