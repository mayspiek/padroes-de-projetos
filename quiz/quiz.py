import json
import random

letras = ['a', 'b', 'c', 'd']

class Quiz:
    def __init__(self):
        with open('./quiz.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            
        self.dificuldades = {}
        
        for dificuldade, categorias in dados["quiz"].items():
            self.dificuldades[dificuldade] = {}
            print(dados["quiz"])
            for categorias, perguntas in categorias.items():
                # categorias = set(categorias)
                print(f'Categoria: {categorias}')
                pass
                # print(categorias)
        #     for categoria, perguntas in categorias.items():
        #         self.dificuldades[dificuldade][categoria] = Categoria(categoria, perguntas)
    
    def selecionar_dificuldade(self):
        """Seleciona a dificuldade do quiz"""
        dificuldades = list(self.dificuldades.keys())
        escolha = input(f"Escolha a dificuldade ({', '.join(dificuldades)}): ").lower()
        if escolha in dificuldades:
            return escolha
        else:
            print("Dificuldade inválida!")
            return self.selecionar_dificuldade()
    
    def selecionar_categoria(self, dificuldade):
        """Seleciona a categoria do quiz"""
        categorias = list(self.dificuldades[dificuldade].keys())
        escolha = input(f"Escolha a categoria ({', '.join(categorias)}): ").lower()
        if escolha in categorias:
            return escolha
        else:
            print("Categoria inválida!")
            return self.selecionar_categoria(dificuldade)
    
    def iniciar_quiz(self):
        """Inicia o quiz permitindo o usuário escolher dificuldade e categoria"""
        dificuldade = self.selecionar_dificuldade()
        categoria = self.selecionar_categoria(dificuldade)
        self.dificuldades[dificuldade][categoria].exibir_perguntas()

class Pergunta:
    def __init__(self, pergunta, alternativas, resposta):
        self.pergunta = pergunta
        self.alternativas = alternativas
        self.resposta = resposta

class Categoria:
    def __init__(self, nome, perguntas):
        self.nome = nome
        self.perguntas = [Pergunta(p["pergunta"], p["alternativas"], p["resposta"]) for p in perguntas]

    def exibir_perguntas(self):
        for pergunta in self.perguntas:
            print(f'{pergunta}')

            alternativas_embaralhadas = self.alternativas.copy()
            random.shuffle(alternativas_embaralhadas)
            
            for i, alt in enumerate(alternativas_embaralhadas):
                print(f'{letras[i]}) {alt}')
            return alternativas_embaralhadas

    def verificar_resposta(self, resposta_usuario, alternativas_embaralhadas):
        index_escolhido = letras.index(resposta_usuario)
        alternativa_escolhida = alternativas_embaralhadas[index_escolhido]
        if alternativa_escolhida == self.resposta:
            return print('\nResposta certa!')
        else:
            return print('\nResposta errada!')

    def escolher_resposta(self, alternativas_embaralhadas):
        resposta_usuario = input("Escolha a alternativa (a, b, c, d): ").lower()
        index_escolhido = letras.index(resposta_usuario)
        alternativa_escolhida = alternativas_embaralhadas[index_escolhido]
        return alternativa_escolhida

if __name__ == '__main__':
    quiz = Quiz()
    # with open('./quiz.json') as f:
    #     data = json.load(f)
    
    # print('Quiz de Futebol')
    # print('Escolha a dificuldade')
    # print('| 1 - Fácil | 2 - Médio | 3 - Difícil |')
    # dificuldade = int(input())

    # if dificuldade == 1:
    #     print('Dificuldade Fácil')
    #     print('Selecione a categoria')

    #     print('| 1 - Clubes | 2 - Geral |')
    #     categoria = int(input())

    #     print('Responda as perguntas abaixo')

    #     # pega as perguntas da categoria geral
    #     for i in data['quiz']['facil']['geral']:
    #         print(f'{i["pergunta"]}')
    #         letras = ['a', 'b', 'c', 'd']

    #         # embaralha as alternativas
    #         alternativas = i['alternativas']
    #         random.shuffle(alternativas)

    #         # exibe as alternativas
    #         for i, alt in enumerate(alternativas):
    #             print(f'{letras[i]}) {alt}')
    #          # Pede a escolha do usuário
    #         resposta_usuario = input("Escolha a alternativa (a, b, c, d): ").lower()
            
    #         # Descobre qual alternativa o usuário escolheu
    #         index_escolhido = letras.index(resposta_usuario)
    #         alternativa_escolhida = alternativas[index_escolhido]
            
    #         # Compara com a resposta correta
    #         if alternativa_escolhida == i['resposta']:
    #             print("Correto!")
    #         else:
    #             print(f"Errado! A resposta correta é: {i['resposta']}")
