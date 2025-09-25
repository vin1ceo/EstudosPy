import time
from abc import ABC, abstractmethod


class Personagem (ABC):
    def __init__(self, nome, vida, pts_ataque, pts_defesa):
        self.__nome = nome
        self.__vida = vida
        self.__pts_ataque = pts_ataque
        self.__pts_defesa = pts_defesa

    @property
    def nome(self):
        return self.__nome

    @property
    def vida(self):
        return self.__vida
    
    @property
    def pts_ataque(self):
        return self.__pts_ataque

    @property
    def pts_defesa(self):
        return self.__pts_defesa
    
    def receber_dano(self, dano):
        dano_sofrido = dano - self.pts_defesa
        if dano_sofrido < 0:
            dano_sofrido = 0
        
        self.__vida -= dano_sofrido
        if self.__vida < 0:
            self.__vida = 0
        print(f"-> {self.nome} sofreu {dano_sofrido:.0f} de dano!")

    def exibir_status(self):
        print(f"STATUS -> Nome: {self.nome}, Vida: {self.vida:.0f}")

    @abstractmethod
    def atacar(self, alvo):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome, vida, pts_ataque, pts_defesa):
        super().__init__(nome, vida, pts_ataque, pts_defesa)
    
    def atacar(self, alvo):
        print(f"🗡️  {self.nome} ataca {alvo.nome} com sua espada!")
        alvo.receber_dano(self.pts_ataque)
    
class Mago(Personagem):
    def __init__(self, nome, vida, pts_ataque, pts_defesa, mana):
        super().__init__(nome, vida, pts_ataque, pts_defesa)
        self.__mana = mana

    @property
    def mana(self):
        return self.__mana
    
    def atacar(self, alvo):
        custo_mana = 10
        if self.__mana >= custo_mana:
            dano_magico = self.pts_ataque * 1.5
            
            # CORREÇÃO 2: Usar __mana (dois underlines)
            self.__mana -= custo_mana
            
            print(f"✨ {self.nome} lança uma bola de fogo em {alvo.nome}!")
            alvo.receber_dano(dano_magico)
        else:
            print(f"💨 {self.nome} tenta, mas não tem mana suficiente para o feitiço!")

# CORREÇÃO 1: A função e o bloco de teste ficam FORA de qualquer classe (sem indentação)
def iniciar_batalha(personagem1, personagem2):
    print(f"\n💥 A BATALHA COMEÇA: {personagem1.nome} VS {personagem2.nome} 💥")
    personagem1.exibir_status()
    personagem2.exibir_status()
    time.sleep(2)

    while personagem1.vida > 0 and personagem2.vida > 0:
        
        print("\n-------------------------")
        personagem1.atacar(personagem2)
        personagem2.exibir_status()
        time.sleep(1)

        # CORREÇÃO 3: Usar <= 0 para a condição de vitória
        if personagem2.vida <= 0:
            break

        print("\n-------------------------")
        personagem2.atacar(personagem1)
        personagem1.exibir_status()
        time.sleep(1)

    print("\n--- FIM DE BATALHA ---")

    if personagem1.vida > 0:
        print(f"🏆 O grande vencedor é {personagem1.nome}!")
    else:
        print(f"🏆 O grande vencedor é {personagem2.nome}!")


# --- Bloco de Testes ---
print("--- CRIAÇÃO DOS PERSONAGENS ---")
guerreiro_forte = Guerreiro(nome="Bárbaro", vida=120, pts_ataque=18, pts_defesa=10)
mago_poderoso = Mago(nome="Feiticeiro", vida=80, pts_ataque=22, pts_defesa=5, mana=50)

iniciar_batalha(guerreiro_forte, mago_poderoso)