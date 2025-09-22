class Veiculo:
    def __init__(self, marca,modelo):
        self.marca = marca
        self.modelo = modelo
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    

    def acelerar(self):
        print("O veiculo está acelerando...")
    

    def frear(self):
        print("O veiculo está freando")


class Carro(Veiculo):
    def __init__(self, marca, modelo, n_portas):
        super().__init__(marca, modelo)
        self.n_portas = n_portas

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def empinar(self):
        print(f"A moto {self.marca} {self.modelo} está empinando")


# Crie os objetos
meu_carro = Carro(marca="Ford", modelo="Ka", n_portas=4)
minha_moto = Moto(marca="Honda", modelo="CB 500", cilindradas=500)

# Teste os métodos do carro
print(meu_carro)
meu_carro.acelerar()
meu_carro.frear()

print("-" * 20) # Uma linha para separar

# Teste os métodos da moto
print(minha_moto)
minha_moto.acelerar()
minha_moto.empinar() # Testando o método exclusivo


        

    
    