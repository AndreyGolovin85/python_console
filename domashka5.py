from random import choice
# Словарь азбуки морзе.
morse_dictionary = {
  "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
  "6": "-....", "7": "--...", "8": "---..", "9": "----.",
  "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.",
  "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.",
  "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-",
  "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..",
  ".": ".-.-.-", ",": "--..--", "?": "..--..", "!": "-.-.--", "-": "-....-", "/": "-..-.",
  "@": ".--.-.", "(": "-.--.", ")": "-.--.-", " ": "/"
}
# Список слов для игры.
list_words = ["code", "bit", "list", "soul", "next", "little", "snake", "well played"]

# Список для хранения ответов.
answers = []


def random_word():
    """
    Фукция берет случайное слово из списка list_words.
    """
    word = choice(list_words)
    return word


def morse_translation(text):
    """
    Функция принимает текст и преобразует его в азбуку морзе.
    """
    # список для хранения преобразованных букв, при каждом вызове функции очищаем список.
    list_morse = []
    for word in text:
        list_morse.append(morse_dictionary[word])

    return f"{' '.join(list_morse)}"


def print_statistic():
    """
    Функция выводит информацию по игровой статистики.
    """
    right_answer = answers.count(True)

    print(f"Всего задачек: {len(answers)}")
    print(f"Отвечено верно: {right_answer}")
    print(f"Отвечено неверно: {len(answers) - right_answer}")


print("Сегодня мы потренируемся расшифровывать азбуку Морзе")
input("Нажмите Enter и начнем ")
print("\n")

for i in range(len(list_words)):
    # Берем случайное слово из списка и возвращаем его.
    random_word_choice = random_word()
    # Преобразовываем слово и помещаем в переменную.
    word_morse = morse_translation(random_word_choice)
    print(f"Слово {i+1}: {word_morse}")
    answer = input()
    if answer.title() == random_word_choice.title():
        print(f"Верно, {random_word_choice.title()}! \n")
        answers.append(True)
    else:
        print(f"Неверно, {random_word_choice.title()}! \n")
        answers.append(False)


print_statistic()
