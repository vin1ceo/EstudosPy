from abc import ABC, abstractmethod

## Classes e funções que fazem o sistema funcionar
class ItemBiblioteca(ABC):
    def __init__(self, titulo):
        self.__titulo = titulo
        self.__disponivel = True

    @property
    def titulo(self):
        return self.__titulo
                                        
    @property
    def disponivel(self):
        return self.__disponivel

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            print(f"O item '{self.titulo}' foi emprestado com sucesso.")
            return True # Retorna True em caso de sucesso
        else:
            print(f"Erro: O item '{self.titulo}' já está emprestado.")
            return False

    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            print(f"O item '{self.titulo}' foi devolvido.")
        else:
            print(f"Aviso: O item '{self.titulo}' já estava disponível!")

    @abstractmethod
    def exibir_detalhes(self):
        pass


class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor):
        super().__init__(titulo)
        self.__autor = autor
    
    @property
    def autor(self):
        return self.__autor
    
    def exibir_detalhes(self):
        print(f"Livro: '{self.titulo}', Autor: {self.autor}")


class Revista(ItemBiblioteca):
    def __init__(self, titulo, edicao):
        super().__init__(titulo)
        self.__edicao = edicao

    @property
    def edicao(self):
        return self.__edicao
    
    def exibir_detalhes(self):
        print(f"Revista: '{self.titulo}', Edição: {self.edicao}")


class Membro():
    def __init__(self, nome):
        self.nome = nome
        self.__itens_emprestados = []

    def pegar_emprestado(self, item):
        sucesso = item.emprestar()
        if sucesso:
            self.__itens_emprestados.append(item)

    def devolver_item(self, item):
        if item in self.__itens_emprestados:
            self.__itens_emprestados.remove(item)
            item.devolver()
        else:
            print(f"Erro: {self.nome} não pode devolver o item '{item.titulo}' pois não o pegou emprestado.")
            
    def listar_itens_emprestados(self):
        print(f"\n--- Itens com {self.nome} ---")
        if not self.__itens_emprestados:
            print("(Nenhum item emprestado no momento)")
            return
        
        for item in self.__itens_emprestados:
            item.exibir_detalhes()


# --- Bloco de Teste ---

# 1. Crie os itens da biblioteca
livro1 = Livro(titulo="O Senhor dos Anéis", autor="J.R.R. Tolkien")
revista1 = Revista(titulo="National Geographic", edicao="Agosto 2025")
livro2 = Livro(titulo="O Guia do Mochileiro das Galáxias", autor="Douglas Adams")

# 2. Crie um membro
membro1 = Membro("Vinicius")

# 3. Simule as ações
print("--- Simulando Empréstimos ---")
membro1.pegar_emprestado(livro1)
membro1.pegar_emprestado(revista1)

# 4. Tente pegar emprestado um item que já está com o membro (deve falhar)
membro1.pegar_emprestado(livro1)

# 5. Liste os itens que o membro pegou (aqui o polimorfismo acontece!)
membro1.listar_itens_emprestados()

# 6. Simule a devolução
print("\n--- Simulando Devolução ---")
membro1.devolver_item(livro1)

# 7. Verifique a lista de itens do membro novamente
membro1.listar_itens_emprestados()

# 8. Tente pegar o livro devolvido (agora deve funcionar)
print("\n--- Tentando pegar o livro devolvido ---")
membro1.pegar_emprestado(livro1)
membro1.listar_itens_emprestados()