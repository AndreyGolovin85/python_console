import json


def load_question():
    """
    функция загружает файл с вопросами
    :return:
    """
    with open("game_question.json", "r", encoding="utf8") as file:
        questions = json.load(file)
    return questions


def show_field(questions):
    """
    Функция выводит на эран игровое поле
    :param questions:
    :return:
    """
    top_level = questions.keys()
    for level in top_level:
        print(level.ljust(15), end="")
        level_questions = questions[level]
        for price, date in level_questions.items():
            if date["asked"]:
                print("   ", end="   ")
            else:
                print(price, end="   ")
        print()


def parse_iput(input_user, questions):
    """
    Функция обрабатывает ввод пользователя
    :param input_user:
    :param questions:
    :return:
    """
    parse_input_user = input_user.split(" ")
    if len(parse_input_user) == 2:
        category = parse_input_user[0].title()
        price = parse_input_user[1]
        if category not in questions:
            return False
        price_category = questions[category]
        if price not in price_category:
            return False
        question_stats = price_category[price]
        if question_stats["asked"]:
            return False
        else:
            question = question_stats["question"]
            answer = question_stats["answer"]
            asked = question_stats["asked"]
            return {"category": category, "price": price, "question": question, "answer": answer, "asked": asked}
    return False


def show_question(text):
    """
    Вывод вопроса на экран
    :param text:
    :return:
    """
    return f"Слово {text} в переводе означает ..."


def show_stats(stats):
    """
    вывод статистики на экран
    :param stats:
    :return:
    """
    return f"У нас закончились вопросы!\nВаш счет: {stats['points']}\nВерных ответов: {stats['correct']}\nНеверных ответов: {stats['incorrect']}"


def save_result(stats):
    """
    запись статистики в файл
    :param stats:
    :return:
    """
    filename = "statistic.json"
    with open(filename, "w") as file:
        json.dump(stats, file)


# Словарь для хранения статистики.
stats = {"points": 0, "correct": 0, "incorrect": 0}


def main():
    """
    Основная функция программы.
    :return:
    """
    questions = load_question()

    while True:
        show_field(questions)
        print("Выберите категорию и стоимость.")
        user_input = input()
        if user_input == "стоп":
            break

        question_parse = parse_iput(user_input, questions)
        category = question_parse.get("category")
        price = question_parse.get("price")
        question = question_parse.get("question")
        answer = question_parse.get("answer")

        if not question_parse:
            print("Такого вопроса нет, попробуйте еще раз!")
            continue
        print(show_question(question))
        answer_input = input()
        if answer_input == answer:
            stats["points"] += int(price)
            stats["correct"] += 1
            print(f"Верно, + {int(price)}. Ваш счет = {stats['points']}\n")
        else:
            stats["points"] -= int(price)
            stats["incorrect"] += 1
            print(f"Неверно, на самом деле – {answer}. – {int(price)}. Ваш счет = {stats['points']}\n")

        questions[category][price]["asked"] = True


main()
print(show_stats(stats))
save_result(stats)
