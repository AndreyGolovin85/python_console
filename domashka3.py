# Приложение для обучения английскому
# Создаем два списка с вопросами и ответами.
questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]
# Переменная счетчик
# Если ответ верный будем прибавлять 1 к вопросам и баллы.
count = 0
scores = 0

# Приветствие и знакомство с пользователем
print("Привет! Предлагаю проверить свои знания английского!")
print("Расскажи, как тебя зовут!")
mame_user = input()
print(f"Привет, {mame_user}, начинаем тренировку!  Наберите 'ready', чтобы начать!")
input_ready = input()

# Логическая часть программы
if input_ready == "ready":
    # Создаем основной цикл приложения.
    for num in range(len(questions)):
        num_right_answer = 3
        answer_right = False
        print(questions[num])
        # Цикл проверки правильных ответов и подсчета баллов.
        while not answer_right:
            answer = input("Ответ: ")
            if answer == answers[num]:
                print(f"Ответ верный.Вы получаете {num_right_answer} баллов!")
                count += 1
                scores += num_right_answer
                # Если ответ верный ставим флаг True.
                answer_right = True
            else:
                num_right_answer -= 1
                if num_right_answer > 0:
                    print(f"Ответ неверный. Осталось попыток: {num_right_answer}, попробуйте еще раз!")
                else:
                    print(f"Увы, но нет. Верный ответ: {answers[num]}")
                    break

    # Вывод статистики
    print(f"Вот и всё, {mame_user}.")
    print(f"Вы ответили на {count} вопросов из {len(questions)} верно.")
    print(f"Вы заработали {scores} баллов")
    print(f"Это {int(count * 100 / len(questions))} процентов.")

else:
    print(f"Кажется, {mame_user}, вы не хотите играть. Очень жаль!")
