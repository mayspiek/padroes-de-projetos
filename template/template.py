from abc import ABC, abstractmethod

class LoginTemplate(ABC):
    def login(self, metodo_autenticacao):
        self.validar_credenciais(metodo_autenticacao)
        self.logar_resultado(metodo_autenticacao)
        self.carregar_preferencias()
        self.redirecionar()
    
    @abstractmethod
    def validar_credenciais(self, metodo_autenticacao):
        pass
    
    def logar_resultado(self, metodo_autenticacao):
        print(f"Salvando email do usuário autenticado via {metodo_autenticacao}...")
    
    def carregar_preferencias(self):
        print("Carregando preferências do usuário...")
    
    @abstractmethod
    def redirecionar(self):
        pass

class LoginFuncionario(LoginTemplate):
    def validar_credenciais(self, metodo_autenticacao):
        print(f"Validando credenciais do funcionário via {metodo_autenticacao}...")
    
    def redirecionar(self):
        print("Redirecionando para o Dashboard...")

class LoginCliente(LoginTemplate):
    def validar_credenciais(self, metodo_autenticacao):
        print(f"Validando credenciais do cliente via {metodo_autenticacao}...")
    
    def redirecionar(self):
        print("Redirecionando para a página Home...")

# Exemplo de uso
if __name__ == "__main__":
    print("--- Login Funcionário ---")
    funcionario = LoginFuncionario()
    funcionario.login("Google")
    
    print("\n--- Login Cliente ---")
    cliente = LoginCliente()
    cliente.login("GitHub")
