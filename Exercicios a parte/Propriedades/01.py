class Produto:
    def __init__(self, nome, preco_inicial, estoque_inicial):
        self.nome = nome
        self.__preco = preco_inicial
        self.__estoque = estoque_inicial

    # --- Propriedade PREÇO ---

    @property # 1. Getter para preco (basta usar @property)
    def preco(self):
        return self.__preco

    @preco.setter # 2. Setter para preco (DEVE ter o mesmo nome da property: "preco")
    def preco(self, novo_preco): # O primeiro argumento é sempre 'self', o segundo é o valor que está sendo atribuído
        if novo_preco >= 0:
            self.__preco = novo_preco
        else:
            print("Erro: O preço deve ser um valor positivo ou zero.")

    # --- Propriedade ESTOQUE --- (mesma lógica do preço)

    @property
    def estoque(self):
        return self.__estoque

    @estoque.setter
    def estoque(self, novo_estoque):
        if novo_estoque >= 0:
            self.__estoque = novo_estoque
        else:
            print("Erro: O estoque não pode ser negativo.")
            
    # Aqui virão os outros métodos (vender, repor_estoque...)

# --- Testando a Classe Corrigida ---
print("Criando o produto...")
p1 = Produto(nome="Caderno", preco_inicial=15.90, estoque_inicial=50)

print(f"Preço inicial: {p1.preco:.2f}")
print(f"Estoque inicial: {p1.estoque}")
print("-" * 20)

print("Tentando colocar um preço negativo...")
p1.preco = -10 # Isso vai chamar o método @preco.setter
print(f"Preço atual: {p1.preco:.2f}") # O valor não deve ter mudado
print("-" * 20)


print("Colocando um preço válido...")
p1.preco = 18.50 # Isso também chama o setter
print(f"Preço atual: {p1.preco:.2f}") # Agora o valor deve mudar
print("-" * 20)

print("Tentando colocar estoque negativo...")
p1.estoque = -5 # Chama o @estoque.setter
print(f"Estoque atual: {p1.estoque}") # Não deve ter mudado
print("-" * 20)