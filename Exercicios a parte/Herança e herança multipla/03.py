class Ave:
    def voar(self):
        print("A criatura está voando alto")

    # Este __str__ agora vai funcionar, pois o Grifo terá atributos!
    def __str__(self):
        # Pequeno ajuste para evitar erro se não houver atributos.
        if not self.__dict__:
            return self.__class__.__name__
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero:
    def correr(self):
        print("A criatura está correndo pelo chão")

class Grifo(Ave, Mamifero):
    # ADICIONANDO O CONSTRUTOR __init__
    def __init__(self, nome, idade, cor):
        # Como as classes-mãe não têm __init__, não precisamos do super() aqui.
        # Apenas criamos os atributos para esta instância.
        self.nome = nome
        self.idade = idade
        self.cor = cor

    def rugir(self):
        print("O grifo está rugindo ferozmente")

# --- TESTANDO O CÓDIGO CORRIGIDO ---

# 1. Criando o objeto SEM 'self' e com os argumentos que o __init__ agora aceita
meu_grifo = Grifo(nome="Grifo Mágico", idade=5, cor="Dourado")

# 2. Agora o print vai funcionar e mostrar os atributos!
print(meu_grifo)

# 3. Os métodos herdados e o exclusivo continuam funcionando
meu_grifo.voar()   # Método herdado de Ave
meu_grifo.correr() # Método herdado de Mamifero 
meu_grifo.rugir()  # Método exclusivo de Grifo

print(f"O nome do grifo é: {meu_grifo.nome}")  # Acessando um atributo