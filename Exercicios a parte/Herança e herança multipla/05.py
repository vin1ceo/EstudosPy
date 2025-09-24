class Conta:
    def __init__(self,numero,titular, saldo = 0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self,valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self,valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def extrato(self):
        print(f"Conta: {self.numero}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: R${self.saldo}")
    
class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo=0):
        super().__init__(numero, titular, saldo)
        
    def render_juros(self, taxa_juros = 0.05):
        taxa_juros = taxa_juros / 100
        juros = self.saldo * taxa_juros
        self.saldo += juros
        print(f"Juros de R${juros} aplicados. Novo saldo: R${self.saldo}")

class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo=0, limite_cheque_especial= 100.00):
        super().__init__(numero, titular, saldo)
        self.limite_cheque_especial = limite_cheque_especial

    def sacar(self, valor):
        if 0 < valor <= self.saldo + self.limite_cheque_especial:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")
    

class Cliente:
    def __init__ (self, nome, cpf, conta: Conta):
        self.nome = nome
        self.cpf = cpf
        self.conta = conta
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    

# --- TESTANDO O CÓDIGO ---
cc = ContaCorrente(numero="1234-5", titular="João Silva", saldo=500.00, limite_cheque_especial=200.00)
cp = ContaPoupanca(numero="6789-0", titular="Maria Oliveira", saldo=1000.00)

cliente1 = Cliente(nome="João Silva", cpf="111.222.333-44", conta=cc)
cliente2 = Cliente(nome="Maria Oliveira", cpf="555.666.777-88", conta=cp)
print(cliente1)
print(cliente2)

print(f"Cliente: {cliente1}")
cliente1.conta.extrato()
print("-" * 20)

cliente1.conta.sacar(600)
cliente1.conta.extrato()
print("-" * 20)

cliente1.conta.sacar(200)
cliente1.conta.extrato()
print("-" * 20)

print(f"Cliente: {cliente2}")
cliente2.conta.extrato()
cliente2.conta.render_juros(5)
print(f"Após render juros:")

cliente2.conta.extrato()