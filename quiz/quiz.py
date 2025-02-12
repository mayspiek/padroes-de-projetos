import json
import random
from abc import ABC, abstractmethod

# 1 - Singleton - Gerenciador do Quiz
class QuizManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(QuizManager, cls).__new__(cls)
            cls._instance.load_questions()
        return cls._instance
    
    def load_questions(self):
        with open("quiz.json", "r", encoding="utf-8") as file:
            self.quiz_data = json.load(file)["quiz"]["dificuldade"]
    
    def get_questions(self, difficulty, category):
        return self.quiz_data[difficulty][category]

# 2 - Factory Method - Criação das Perguntas
class QuestionFactory:
    @staticmethod
    def create_question(question_data):
        return Question(question_data)

# Classe de Pergunta
class Question:
    def __init__(self, data):
        self.text = data["pergunta"]
        self.options = data["alternativas"]
    
    def display(self):
        print(self.text)
        for idx, option in enumerate(self.options, 1):
            print(f"{idx}. {option['alt']}")
    
    def check_answer(self, user_answer):
        return self.options[user_answer - 1]["correct"]

# 3 - Strategy - Diferentes modos de quiz
class QuizStrategy(ABC):
    @abstractmethod
    def execute(self, questions):
        pass

class RandomQuizStrategy(QuizStrategy):
    def execute(self, questions):
        return random.sample(questions, len(questions))

class OrderedQuizStrategy(QuizStrategy):
    def execute(self, questions):
        return questions

# 4 - Observer - Observa respostas
class QuizObserver:
    def update(self, question, correct):
        if correct:
            print("Resposta correta!\n")
        else:
            print("Resposta incorreta.\n")

# 5 - Template Method - Fluxo do Quiz
class Quiz:
    def __init__(self, difficulty, category, strategy):
        self.manager = QuizManager()
        self.questions = self.manager.get_questions(difficulty, category)
        self.strategy = strategy
        self.observer = QuizObserver()
    
    def run(self):
        ordered_questions = self.strategy.execute(self.questions)
        for q_data in ordered_questions:
            question = QuestionFactory.create_question(q_data)
            question.display()
            try:
                user_answer = int(input("Sua resposta: "))
                correct = question.check_answer(user_answer)
                self.observer.update(question, correct)
            except (ValueError, IndexError):
                print("Resposta inválida!\n")

# Execução do Quiz
if __name__ == "__main__":
    difficulty = input("Escolha a dificuldade (facil, medio, dificil): ")
    category = input("Escolha a categoria (geral, clubes): ")
    strategy_choice = input("Modo de quiz (1- Aleatório, 2- Ordenado): ")
    strategy = RandomQuizStrategy() if strategy_choice == "1" else OrderedQuizStrategy()
    
    quiz = Quiz(difficulty, category, strategy)
    quiz.run()
