from abc import ABC, abstractmethod

class Dispositivo(ABC):
    total_dispositivos = 0

    ##Constutor
    def __init__(self,localizacao):  
        self.__localizacao = localizacao
        self.__ligado = False
        Dispositivo.total_dispositivos += 1

    @property
    def localizacao(self):
        return self.__localizacao
    
    @property
    def ligado(self):
        return self.__ligado
    
    def ligar(self):
        if not self.__ligado:
            self.__ligado = True
            print(f"Dispositivo em '{self.localizacao}' ligado!")
        else:
            print(f"O dispositivo em '{self.localizacao}' já está ligado!")
    
    def desligar(self):
        if self.__ligado:
            self.__ligado = False
            print("Dispositivo desligado!")
        else:
            print("O dispositivo já está desligado!!!!")
            return False
    
    @abstractmethod
    def status(self):
        pass
            

class Luz(Dispositivo):
    def __init__(self, localizacao, intensidade):
        super().__init__(localizacao)
        self.__intensidade = intensidade

    @property
    def intensidade(self):
        return self.__intensidade
    
    @intensidade.setter
    def intensidade(self, nova_intensidade):
        if 0 <= nova_intensidade <= 100:
            self.__intensidade = nova_intensidade
        else:
            print("Erro! A intensidade tem que estar entre 0 e 100") 

    
    def status(self):
        estado = "Ligada" if self.ligado else "Desligada"
        return f"Luz da {self.localizacao}: {estado}, Intensidade: {self.intensidade}%"
    
class Termostato(Dispositivo):
    def __init__(self, localizacao, temperatura=21):
        super().__init__(localizacao)
        self.temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, nova_temperatura):
        if 15 <= nova_temperatura <= 30:
            self.__temperatura = nova_temperatura
        else:
            print("Erro: A temperatura deve ser um valor entre 15°C e 30°C.")
            
    def status(self):
        estado = "Ligado" if self.ligado else "Desligado"
        return f"Termostato da {self.localizacao}: {estado}, Temperatura: {self.temperatura}°C"

class Comodo():
    def __init__(self, nome_comodo):
        self.nome_comodo = nome_comodo
        self.__dispositivos = [] # Começa com uma lista vazia de dispositivos

    def adicionar_dispositivo(self, dispositivo):
        self.__dispositivos.append(dispositivo)
        print(f"{dispositivo.__class__.__name__} adicionado(a) ao cômodo '{self.nome_comodo}'.")

    def ligar_tudo(self):
        print(f"\n--- Ligando todos os dispositivos em '{self.nome_comodo}' ---")
        for dispositivo in self.__dispositivos:
            dispositivo.ligar()

    def desligar_tudo(self):
        print(f"\n--- Desligando todos os dispositivos em '{self.nome_comodo}' ---")
        for dispositivo in self.__dispositivos:
            dispositivo.desligar()

    # A função polimórfica!
    def gerar_relatorio(self):
        print(f"\n--- Relatório do Cômodo: {self.nome_comodo} ---")
        for dispositivo in self.__dispositivos:
            # Não importa se é Luz ou Termostato, chamamos o método status()
            # e o próprio objeto sabe o que fazer.
            print(dispositivo.status())

    # 1. Crie um cômodo
sala = Comodo("Sala de Estar")

# 2. Crie os dispositivos para a sala
luz_sala = Luz(localizacao="Sala de Estar", intensidade=70)
termostato_sala = Termostato(localizacao="Sala de Estar", temperatura=22)

# 3. Adicione os dispositivos ao cômodo
sala.adicionar_dispositivo(luz_sala)
sala.adicionar_dispositivo(termostato_sala)

# 4. Gere um relatório inicial
sala.gerar_relatorio()

# 5. Ligue tudo
sala.ligar_tudo()

# 6. Altere um valor individual
print("\n--- Alterando a temperatura ---")
termostato_sala.temperatura = 24
termostato_sala.temperatura = 40 # Tentativa inválida

# 7. Gere o relatório final
sala.gerar_relatorio()

# 8. Verifique o contador de classe
print(f"\nTotal de dispositivos criados no sistema: {Dispositivo.total_dispositivos}")