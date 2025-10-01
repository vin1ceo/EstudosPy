class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = float(preco)
        self.quantidade = quantidade
    

    def __str__(self):


        return f"Nome: {self.nome}\nPreço: R${self.preco:.2f}\n Quantidade: {self.quantidade}"
    

p1 = Produto(nome="Coca-cola", preco= 4.50, quantidade=10)

print(p1)