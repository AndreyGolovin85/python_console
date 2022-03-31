class Question:
    def __init__(self, questions, answer, difficult):
        self.question = questions
        self.answer = answer
        self.difficult = difficult

        self.asked = False
        self.user_answer = None
        self.max_difficult = 5

    def get_points(self):
        """
        Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.difficult * 10

    def is_correct(self) -> bool:
        """
        Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        return self.answer == self.user_answer

    def build_question(self):
        """
        Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f"Вопрос: {self.question}?\nСложность {self.difficult}/{self.max_difficult}"

    def build_positive_or_negative_feedback(self):
        """
        Возвращает :
        Ответ верный, получено __ баллов
        Возвращает : Ответ неверный, верный ответ __
        """
        if self.is_correct():
            return f"Ответ верный, получено {self.get_points()} баллов"
        return f"Ответ неверный, верный ответ {self.answer}"
