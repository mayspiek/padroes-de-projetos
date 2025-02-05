from abc import ABC, abstractmethod
from typing import final

class LoginTemplate(ABC):
    @final
    # template de fato, especificando os passos do login
    def login(self, metodo_autenticacao: str):
        self.validar_credenciais(metodo_autenticacao)
        self.logar_resultado(metodo_autenticacao)
        self.carregar_preferencias()
        self.redirecionar()
    
    # abstrato: a subclasse deve implementar
    @abstractmethod
    def validar_credenciais(self, metodo_autenticacao: str):
        pass
    
    def logar_resultado(self, metodo_autenticacao: str):
        print(f"Salvando email do usuário autenticado via {metodo_autenticacao}...")
    
    def carregar_preferencias(self):
        print("Carregando preferências do usuário...")
    
    # abstrato: a subclasse deve implementar
    @abstractmethod
    def redirecionar(self):
        pass

# implementação do template
class LoginFuncionario(LoginTemplate):
    def validar_credenciais(self, metodo_autenticacao: str):
        print(f"Validando credenciais do funcionário via {metodo_autenticacao}...")
    
    def redirecionar(self):
        print("Redirecionando para o Dashboard...")

# implementação do template
class LoginCliente(LoginTemplate):
    def validar_credenciais(self, metodo_autenticacao: str):
        print(f"Validando credenciais do cliente via {metodo_autenticacao}...")
    
    def redirecionar(self):
        print("Redirecionando para a página Home...")

if __name__ == "__main__":
    print("--- Login Funcionário (Google) ---")
    funcionario = LoginFuncionario()
    funcionario.login("Google")
    
    print("\n--- Login Cliente (GitHub) ---")
    cliente = LoginCliente()
    cliente.login("GitHub")
