class FiguraGeo:
    def __init__(self):
        pass

    def calcular_area(self):
        print("Método não implementado")
    def calcular_perimetro(self):
        print("Método não implementado")

class Retangulo(FiguraGeo):
    def __init__(self, base, altura):
        super().__init__

        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2* (self.base + self.altura)
    

# Criando um objeto da classe Retangulo
meu_retangulo = Retangulo(base=10, altura=5)

# Usando os métodos para obter os valores
area = meu_retangulo.calcular_area()
perimetro = meu_retangulo.calcular_perimetro()

# Agora você pode imprimir os resultados
print(f"A área do retângulo é: {area}")
print(f"O perímetro do retângulo é: {perimetro}")
