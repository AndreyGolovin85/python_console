# Программа угадай слрово.
# Создаем словари с вариантами сложности.
words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

# Словарь с уровнями пользователя.
levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}

"""
Создадим пустой словарь в который будут записаны ответы пользователя,
для дальнейшего подсчета правильных и неправильных ответов.
"""
answers = {}

# Выбор сложности слов
print("Выберите уровень сложности: 'легкий, средний, сложный'.")
input_user = input().lower()
if input_user == "легкий":
    dict_level = words_easy
elif input_user == "средний":
    dict_level = words_medium
elif input_user == "сложный":
    dict_level = words_hard
print(f"Выбран уровень сложности {input_user}, мы предложим"
      f" {len(dict_level)} слов, подберите перевод.")

# Запускаем основной цикл игры.
for key, value in dict_level.items():
    print("\n")
    input("Нажмите Enter для продолжения")
    print(f"{key}, {len(value)} букв, начинается на {value[0]}...")
    # Ввод ответа пользователем и проверка ответа.
    input_answer = input().lower()
    if input_answer == value:
        print(f"Верно, {key.title()} - это {value}.")
        answers[key] = True
    else:
        print(f"Неверно, {key.title()} - это {value}.")
        answers[key] = False
    print(answers)

sum_right_answer = 0
print("Правильно отвечены слова:")
for key in answers.keys():
    if answers[key]:
        sum_right_answer += 1
        print(key)

print("Неправильно отвечены слова:")
for key in answers.keys():
    if not answers[key]:
        print(key)

print("Ваш ранг:")
print(levels[sum_right_answer])
