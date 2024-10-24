class IEnvio():
    def enviar(self, peso, valor):
        self.peso = peso
        self.valor = valor
    
class EnvioAereo(IEnvio):
    def enviar(self, peso, valor):
        frete = 25
        print(f'- Valor do produto: R${valor} \n- Peso do produto: {peso}kg \n- Frete: R${frete} \n- Total: R${valor + frete}')

class EnvioExpresso(IEnvio):
    def enviar(self, peso, valor):
        frete = 15
        print(f'- Valor do produto: R${valor} \n- Peso do produto: {peso}kg \n- Frete: R${frete} \n- Total: R${valor + frete}')

class EnvioCorreios(IEnvio):
    def enviar(self, peso, valor):
        frete = 10
        print(f'- Valor do produto: R${valor} \n- Peso do produto: {peso}kg \n- Frete: R${frete} \n- Total: R${valor + frete}')


def main():
    coisa1 = EnvioAereo()
    coisa1.enviar(2, 50)
    pass

if __name__ == '__main__':
    main()