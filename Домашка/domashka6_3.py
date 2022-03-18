list_letters = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м",
                "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]


def shift_encode(string: str) -> str:
    """Функция шифрует строку"""
    list_encode = []
    for let in string:
        if let == "я":
            list_encode.append(list_letters[0])
        else:
            list_encode.append(list_letters[list_letters.index(let) + 1])

    return "".join(list_encode)


def shift_decode(string: str) -> str:
    """Функция дешифрует строку"""
    list_encode = []
    for let in string:
        if let == "а":
            list_encode.append(list_letters[32])
        else:
            list_encode.append(list_letters[list_letters.index(let) - 1])

    return "".join(list_encode)


input_word = input()
print(shift_encode(input_word))
print(shift_decode(shift_encode(input_word)))
