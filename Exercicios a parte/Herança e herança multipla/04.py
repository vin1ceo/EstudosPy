class DispositivoEletronico:
    def __init__(self, modelo, voltagem):
        self.modelo = modelo
        self.voltagem = voltagem
        self.ligado = False
    
    def __str__(self):
        if not self.__dict__:
            return self.__class__.__name__
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f'{self.modelo} está ligado')
        else:
            print(f'{self.modelo} já está ligado')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f'{self.modelo} está desligado')
        else:
            print(f'{self.modelo} já está desligado')

class Impressora:
    # Construtor adicionado
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def imprimir(self):
        print(f"Imprimindo do {self.marca} {self.modelo}...")

# A herança continua a mesma
class ImpressoraMultifuncional(DispositivoEletronico, Impressora):
    def __init__(self, voltagem, marca, modelo):
        # Chama o __init__ de CADA classe mãe com os argumentos corretos
        DispositivoEletronico.__init__(self, modelo, voltagem)
        Impressora.__init__(self, marca, modelo)
        
    def digitalizar(self):
        print("Digitalizando documento...")

# --- Testando o código corrigido ---

impressora = ImpressoraMultifuncional(voltagem=110, marca="HP", modelo="LaserJet Pro")

print(impressora)
impressora.ligar()
impressora.imprimir()
impressora.digitalizar()
impressora.desligar()

# Acessando atributos de ambas as classes-mãe
print(f"Voltagem do equipamento: {impressora.voltagem}v")
print(f"Marca do equipamento: {impressora.marca}")