error_dict = {
    "out": "Вы вышли из системы",
    "unknown": "Неизвестная ошибка",
    "timeout": "Система долго не отвечает",
    "noaccess": "У вас нет доступа в этот раздел",
    "robot": "Ваши действия похожи на робота",
}


def get_errors(*word) -> list:
    list_return = []
    for x in word:
        list_return.append(error_dict[x])
    return list_return


word = [word for word in input().split(" ")]
print(get_errors(*word))
