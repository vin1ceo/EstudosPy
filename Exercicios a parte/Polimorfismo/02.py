from abc import ABC, abstractmethod
import math

class Forma(ABC):

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass



class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.__largura = largura
        self.__altura = altura

    @property
    def largura(self):
        return self.__largura
    
    @property
    def altura(self):
        return self.__altura
    
    def calcular_area(self):
        return self.__largura * self.__altura
    
    def calcular_perimetro(self):
        return 2 * (self.__largura + self.__altura)


class Circulo(Forma):
    def __init__(self,raio):
        self.__raio = raio

    @property
    def raio(self):
        return self.__raio
    
    def calcular_area(self):
        return math.pi * (self.__raio ** 2)
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.__raio
    


##

# --- A FUNÇÃO POLIMÓRFICA ---
def imprimir_relatorio(formas):
    area_total = 0
    
    print("--- Relatório de Formas ---")

    for forma in formas:
        area = forma.calcular_area()
        perimetro = forma.calcular_perimetro()
        area_total += area
        
        print(f"\n* Forma: {forma.__class__.__name__}")
        print(f"  - Área: {area:.2f}")
        print(f"  - Perímetro: {perimetro:.2f}")

    print("\n-----------------------------")
    print(f"Área Total de todas as formas: {area_total:.2f}")


# --- BLOCO DE TESTE (ONDE TUDO ACONTECE) ---

# 1. Crie os objetos
retangulo1 = Retangulo(largura=10, altura=5)
circulo1 = Circulo(raio=7)
retangulo2 = Retangulo(largura=8, altura=3)

# 2. Crie a lista com as diferentes formas
minha_colecao_de_formas = [retangulo1, circulo1, retangulo2]

# 3. Chame a função para gerar o relatório
imprimir_relatorio(minha_colecao_de_formas)
    


        
        
