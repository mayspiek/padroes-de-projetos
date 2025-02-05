from abc import ABC, abstractmethod


class BaseUser(ABC):
    def __init__(self, name):
        self.name = name
        self.permissions = []

    @abstractmethod
    def show_permissions(self):
        pass

class User(BaseUser):
    def __init__(self, name):
        super().__init__(name)

    def show_permissions(self):
        print(f"Permissões do Usuário {self.name}:")
        for permission in self.permissions:
            print(f"- {permission}")
        
class Admin(BaseUser):
    def __init__(self, name):
        super().__init__(name)
        
    def show_permissions(self):
        print(f"Permissões do Administrador {self.name}:")
        for permission in self.permissions:
            print(f"- {permission}")
            
class UserConstructor:
    def create_user(self, name, user_type):
        if user_type == 'Admin':
            return Admin(name)
        elif user_type == 'User':
            return User(name)
        else:
            raise ValueError("Tipo de usuário inválido")
        
class PermissionsBuilder():
    def __init__(self, name, user_type):
        self.user = UserConstructor().create_user(name, user_type)
       
    def reset_permissions(self):
        self.user.permissions = []
        
    def remove_user_permission(self):
        self.user.permissions.append('Permição de remover usuários.')
        return self
    
    def edit_user_permission(self):
        self.user.permissions.append('Permição de editar usuários.')
        return self
    
    def add_company_permission(self):
        self.user.permissions.append('Permição de adicionar empresas.')
        return self
    
    def remove_company_permission(self):
        self.user.permissions.append('Permição de remover empresas.')
        return self
    
    def change_others_password_permission(self):
        self.user.permissions.append('Permição de alterar senha de outros usuários.')
        return self
    
    def reset_password_permission(self):
        self.user.permissions.append('Permição de resetar própria senha.')
        return self
    
    def edit_self_permission(self):
        self.user.permissions.append('Permição de editar própria conta.')
        return self
    
    def build(self):
        return self.user
    
if __name__ == '__main__':
    admin = (PermissionsBuilder('João', 'Admin')
                .remove_user_permission()
               .edit_user_permission()
               .add_company_permission()
               .remove_company_permission()
               .change_others_password_permission()
               .build())
    
    admin.show_permissions()
    
    user = (PermissionsBuilder('Maria', 'User')
               .edit_self_permission()
               .add_company_permission()
               .reset_password_permission()
               .build())
    
    user.show_permissions()
