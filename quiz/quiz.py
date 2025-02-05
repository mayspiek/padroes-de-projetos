import json
from abc import ABC, abstractmethod

# 1 - Singleton para garantir que só haja uma instância do Quiz
class Quiz:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Quiz, cls).__new__(cls)
            cls._instance._dados = None
        return cls._instance

    def carregar_dados(self, caminho_arquivo):
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            self._dados = json.load(arquivo)

    @property
    def dados(self):
        if self._dados is None:
            raise ValueError("Os dados do quiz ainda não foram carregados.")
        return self._dados


# 2 - Builder para construir quizzes com base na dificuldade e categoria
class QuizBuilder:
    def __init__(self):
        self.dificuldade = None
        self.categoria = None

    def set_dificuldade(self, dificuldade):
        if(dificuldade == "1"):
            dificuldade = "facil"
        elif(dificuldade == "2"):
            dificuldade = "medio"
        elif(dificuldade == "3"):
            dificuldade = "dificil"
        else: 
            raise ValueError("Dificuldade inválida")
        self.dificuldade = dificuldade
        return self

    def set_categoria(self, categoria):
        if(categoria == "1"):
            categoria = "geral"
        elif(categoria == "2"):
            categoria = "clubes"
        else: 
            raise ValueError("Categoria inválida")
        self.categoria = categoria
        return self

    def construir(self):
        if not self.dificuldade or not self.categoria:
            raise ValueError("Dificuldade e categoria devem ser definidas.")
        
        quiz = Quiz()
        perguntas = quiz.dados["quiz"]["dificuldade"].get(self.dificuldade, {}).get(self.categoria, [])
        return Categoria(self.categoria, perguntas)


# Categoria representa um conjunto de perguntas
class Categoria:
    def __init__(self, nome, perguntas):
        self.nome = nome
        self.perguntas = [PerguntaFactory.criar(p) for p in perguntas]


# 3 - Factory para criar instâncias de Pergunta
class PerguntaFactory:
    @staticmethod
    def criar(dados_pergunta):
        return Pergunta(
            pergunta=dados_pergunta["pergunta"],
            alternativas=dados_pergunta["alternativas"]
        )


class Pergunta:
    def __init__(self, pergunta, alternativas):
        self.pergunta = pergunta
        self.alternativas = alternativas

    def exibir(self):
        print(f"\n{self.pergunta}")
        for i, alt in enumerate(self.alternativas, start=1):
            print(f"{i}. {alt['alt']}")

    def verificar_resposta(self, indice_resposta):
        return self.alternativas[indice_resposta]["correct"]


# 4 - Observer para pontuação
class ObservadorPontuacao(ABC):
    @abstractmethod
    def atualizar(self, acertos, total):
        pass


class Pontuacao(ObservadorPontuacao):
    def __init__(self):
        self.acertos = 0
        self.erros = 0

    def atualizar(self, acertos, total):
        self.acertos += acertos
        self.erros += total - acertos

    def exibir_resultado(self):
        print("\nRESULTADO FINAL:")
        print(f"Acertos: {self.acertos}")
        print(f"Erros: {self.erros}")


# Classe para gerenciar o fluxo do quiz
class GerenciadorQuiz:
    def __init__(self, categoria):
        self.categoria = categoria
        self.pontuacao = Pontuacao()

    def iniciar(self):
        total_perguntas = len(self.categoria.perguntas)
        acertos = 0

        for pergunta in self.categoria.perguntas:
            pergunta.exibir()
            resposta = int(input("Escolha a resposta (número): ")) - 1
            if pergunta.verificar_resposta(resposta):
                print("Correto!")
                acertos += 1
            else:
                print("Errado!")

        self.pontuacao.atualizar(acertos, total_perguntas)
        self.pontuacao.exibir_resultado()



if __name__ == '__main__':
    quiz = Quiz()
    quiz.carregar_dados('./quiz.json')

    builder = QuizBuilder()
    
    dificuldade = input("Escolha a dificuldade (1 - Fácil, 2 - Médio, 3 - Difícil): ")
    categoria = input("Escolha a categoria (1 - Geral, 2 - Clubes): ")
    quizbuildado = builder.set_dificuldade(dificuldade).set_categoria(categoria).construir()

    gerenciador = GerenciadorQuiz(quizbuildado)
    gerenciador.iniciar()
