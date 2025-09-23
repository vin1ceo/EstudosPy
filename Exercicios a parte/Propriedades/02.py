class Televisao:
    def __init__(self):
        self.__ligada = False
        self.__canal = 1
        self.__volume = 10

    @property
    def ligada(self):
        return "Ligada" if self.__ligada else "Desligada"
    
    def ligar(self):
        if not self.__ligada:
            self.__ligada = True
            print("A TV está ligada")
        else:
            print("A TV já está ligada")
    
    def desligar(self):
        if self.__ligada:
            self.__ligada = False
            print("A TV está desligada")
        else:
            print("A TV já está desligada")

    @property
    def canal(self):
        return self.__canal
    
    @canal.setter
    def canal(self, novo_canal):
        if self.__ligada:

            if 1 <= novo_canal <= 99:
                self.__canal = novo_canal
                print(f"Canal alterado para {self.__canal}")
            else:
                print("Canal invalido. Por favor escolha um  canal entre 1 e 99")
        else:
            print("Tv desligada.")
    
    @property
    def volume(self):
        return self.__volume
    
    @volume.setter
    def volume(self, novo_volume):
        if self.__ligada:
            if 0 <= novo_volume <= 100:
                self.__volume = novo_volume
                print(f"Volume alterado para {self.__volume}")
            else:
                print(f"Volume inválido.")
        else:
            print("Tv desligada")

# --- Bloco de Teste ---
tv = Televisao()

# 1. Tenta mudar o canal com a TV desligada (deve falhar)
print("--- TV Desligada ---")
tv.canal = 5
print(f"Canal atual: {tv.canal}")

# 2. Liga a TV
print("\n--- Ligando a TV ---")
tv.ligar()

# 3. Tenta mudar o canal com a TV ligada (deve funcionar)
tv.canal = 10
print(f"Canal atual: {tv.canal}")

# 4. Tenta colocar um canal inválido (deve falhar)
tv.canal = 150
print(f"Canal atual: {tv.canal}")

# 5. Testa o volume
print(f"\nVolume atual: {tv.volume}")
tv.volume = 80
print(f"Novo volume: {tv.volume}")
tv.volume = 120 # Tenta colocar volume inválido
print(f"Volume final: {tv.volume}")

# 6. Desliga a TV
print("\n--- Desligando a TV ---")
tv.desligar()
        

