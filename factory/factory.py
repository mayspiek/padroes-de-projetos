from abc import ABC, abstractmethod

class NPC(ABC):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def exibir(self):
        print(f'| [NPC]Nome: {self.name} - Dano: {self.damage} |\n')

class Player(ABC):
    def __init__(self, name, hp, defense):
        self.name = name
        self.hp = hp
        self.defense = defense

    def exibir(self):
        print(f'| [Player]Nome: {self.name} - HP: {self.hp} - Defesa: {self.defense} |\n')

class NPCFactory(ABC):
    @abstractmethod
    def create(name, damage):
        return NPC(name, damage)
        
class PlayerFactory(ABC):
    @abstractmethod
    def create(name, hp, defense):
        return Player(name, hp, defense)
    
def battle(player, npc):
    print(f'| {player.name} VS {npc.name} |')
    print(f'| {player.name} HP: {player.hp} | {npc.name} Dano: {npc.damage} |')
    print(f'{npc.name} ataca {player.name} com {npc.damage} de dano mas ele tem {player.defense} de defesa')
    player.hp -= (npc.damage - player.defense)
    print(f'{player.name} fica com HP: {player.hp}')

def main():
    dragao = NPCFactory.create('Dragon', 15)
    esqueleto = NPCFactory.create('Esqueleto', 10)

    mario = PlayerFactory.create('Mario', 100, 8)

    dragao.exibir()
    esqueleto.exibir()

    battle(mario, dragao)

if __name__ == '__main__':
    main()
