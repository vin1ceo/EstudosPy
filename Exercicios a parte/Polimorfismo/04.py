class Usuario():
    total_usuarios = 0

    def __init__(self,email, nome):
        self.email = email
        self.nome = nome
        Usuario.total_usuarios += 1

    @classmethod
    def mostrar_total(cls):
        print(f"print {cls.total_usuarios}")

# --- Bloco de Teste ---
print(f"Total de usuários no início: {Usuario.total_usuarios}")

# Criamos os usuários usando a nova ordem (nome, email)
u1 = Usuario(nome="Alice", email="alice@email.com")
u2 = Usuario(nome="Bob", email="bob@email.com")

print(f"Total de usuários depois de criar dois: {Usuario.total_usuarios}")

u3 = Usuario(nome="Charlie", email="charlie@email.com")

# Usando o método de classe para mostrar o total final
Usuario.mostrar_total()