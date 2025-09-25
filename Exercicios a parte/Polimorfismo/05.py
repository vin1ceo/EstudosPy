class ContaPoupanca():
    # Perfeito! Atributo de classe, compartilhado por todos.
    taxa_juros = 0.005

    def __init__(self, titular, saldo_inicial):
        # Atributos de instância, únicos para cada conta.
        self.titular = titular
        # Correção 1: Renomeando para 'saldo' para clareza.
        self.saldo = saldo_inicial

    # Correção 2: Este deve ser um método de INSTÂNCIA, pois modifica o saldo de CADA conta.
    # Removemos o @classmethod e usamos 'self'.
    def render_juros_mensal(self):
        # Correção 3: O juro é uma porcentagem DO SALDO ATUAL.
        # Acessamos o atributo de classe através de 'self' ou 'ContaPoupanca'.
        juros = self.saldo * self.taxa_juros
        
        # Somamos os juros ao saldo DESTE objeto específico.
        self.saldo += juros
        print(f"Juros de R${juros:.2f} aplicados na conta de {self.titular}.")

# --- O Bloco de Teste agora vai funcionar perfeitamente ---

conta1 = ContaPoupanca("João", 1000)
conta2 = ContaPoupanca("Maria", 2500)

print(f"Taxa de juros atual: {ContaPoupanca.taxa_juros * 100:.1f}%")
conta1.render_juros_mensal()
conta2.render_juros_mensal()
print(f"Saldo de João: R${conta1.saldo:.2f}")
print(f"Saldo de Maria: R${conta2.saldo:.2f}")

print("\n--- O Banco Central mudou a taxa de juros! ---")
# Mudamos o atributo de CLASSE, e isso afetará todas as instâncias.
ContaPoupanca.taxa_juros = 0.006

print(f"Nova taxa de juros: {ContaPoupanca.taxa_juros * 100:.1f}%")
# A mesma chamada de método agora usa a nova taxa para o cálculo.
conta1.render_juros_mensal()
conta2.render_juros_mensal()
print(f"Novo saldo de João: R${conta1.saldo:.2f}")
print(f"Novo saldo de Maria: R${conta2.saldo:.2f}")