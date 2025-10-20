class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.preco = float(preco)
        self.quantidade = quantidade

  # --- Propriedades ---

    # Propriedade somente leitura para o nome (não faz sentido mudar o nome de um produto depois de criado)
    @property
    def nome(self):
        return self.__nome

    # Propriedade com getter e setter para o preço
    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco
        else:
            print(f"Erro: O preço ('{novo_preco}') não pode ser negativo.")
    
    # Propriedade com getter e setter para a quantidade
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, nova_quantidade):
        if isinstance(nova_quantidade, int) and nova_quantidade >= 0:
            self.__quantidade = nova_quantidade
        else:
            print(f"Erro: A quantidade ('{nova_quantidade}') deve ser um número inteiro e positivo.")

    def __str__(self):
        # O __str__ continua funcionando perfeitamente, pois ele usa as propriedades!
        return f"{self.nome} (R$ {self.preco:.2f}) - Estoque: {self.quantidade}"
    
class MaquinaDeVendas:
    def __init__(self):
        self.__estoque = {}
        self.__credito = 0


    def adicionar_produto(self,produto):
        
        self.__estoque[produto.nome] = produto
    
        print(f"-> Produto '{produto.nome}' adicionado ao estoque da máquina.")

    def exibir_estoque(self):
        print("--- PRODUTOS DISPONÍVEIS ---")
        for produto in self.__estoque.values():
            print(produto)

    print("----------------------------")

    def inserir_dinheiro(self,valor):
        
        if valor > 0:
            self.__credito += valor
            print(f"Crédito atual: R$ {self.__credito:.2f}")
        else:
            print("Erro: Por favor, insira um valor positivo.")


     

