class IEnvio():
    def enviar(self, peso, valor):
        self.peso = peso
        self.valor = valor
    
class EnvioAereo(IEnvio):
    def enviar(self, peso, valor):
        frete = 25
        print(f'FRETE AÉREO \n- Valor do produto: R${valor} \n- Peso do produto: {peso}kg \n- Frete: R${frete} \n- Total: R${valor + frete}')

class EnvioExpresso(IEnvio):
    def enviar(self, peso, valor):
        frete = 15
        print(f'ENVIO EXPRESSO \n- Valor do produto: R${valor} \n- Peso do produto: {peso}kg \n- Frete: R${frete} \n- Total: R${valor + frete}')

class EnvioCorreios(IEnvio):
    def enviar(self, peso, valor):
        frete = 10
        print(f'ENVIO CORREIOS \n- Valor do produto: R${valor} \n- Peso do produto: {peso}kg \n- Frete: R${frete} \n- Total: R${valor + frete}')

if __name__ == '__main__':
    coisa1 = EnvioAereo()
    coisa1.enviar(2, 50)