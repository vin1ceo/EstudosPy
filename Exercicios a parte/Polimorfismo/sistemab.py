import tkinter as tk
from tkinter import messagebox # Usaremos para pop-ups
from abc import ABC, abstractmethod


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
            return True # Retorna True em caso de sucesso
        else:
            return False

    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            return True
        return False

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
        return f"Livro: '{self.titulo}', Autor: {self.autor}"


class Membro():
    def __init__(self, nome):
        self.nome = nome
        self.__itens_emprestados = []

    def pegar_emprestado(self, item):
        sucesso = item.emprestar()
        if sucesso:
            self.__itens_emprestados.append(item)
            return True
        return False

    def devolver_item(self, item):
        if item in self.__itens_emprestados:
            self.__itens_emprestados.remove(item)
            item.devolver()
            return True
        return False

# --------------------------------------------------------------------
# PARTE 2: A INTERFACE GRÁFICA (GUI com Tkinter)
# --------------------------------------------------------------------

# --- Criando os objetos que nosso sistema vai gerenciar ---
livro1 = Livro(titulo="O Senhor dos Anéis", autor="J.R.R. Tolkien")
membro1 = Membro("Vinicius")

# --- Funções que serão chamadas pelos botões ---

def acao_emprestar():
    # A interface chama o método do cérebro
    if membro1.pegar_emprestado(livro1):
        # A interface atualiza o texto na tela com a resposta
        label_status.config(text=f"'{livro1.titulo}' emprestado para {membro1.nome}!")
        messagebox.showinfo("Sucesso", "Livro emprestado!")
    else:
        label_status.config(text=f"'{livro1.titulo}' não está disponível.")
        messagebox.showerror("Erro", "O livro já está emprestado!")

def acao_devolver():
    if membro1.devolver_item(livro1):
        label_status.config(text=f"'{livro1.titulo}' foi devolvido.")
        messagebox.showinfo("Sucesso", "Livro devolvido!")
    else:
        label_status.config(text=f"'{livro1.titulo}' já estava na biblioteca.")
        messagebox.showwarning("Aviso", "Você não pode devolver um livro que não pegou.")


# --- Construção da Janela ---

# 1. Cria a janela principal
janela = tk.Tk()
janela.title("Mini Sistema de Biblioteca")
janela.geometry("1080x720") # Define o tamanho da janela

# 2. Cria os widgets (botões, textos, etc.)
label_titulo = tk.Label(janela, text=f"Livro Disponível: {livro1.titulo}", font=("Helvetica", 12))
botao_emprestar = tk.Button(janela, text="Pegar Emprestado", command=acao_emprestar)
botao_devolver = tk.Button(janela, text="Devolver", command=acao_devolver)
label_status = tk.Label(janela, text="Bem-vindo!", bd=1, relief=tk.SUNKEN, anchor=tk.W)

# 3. Adiciona os widgets à janela (empacota)
label_titulo.pack(pady=10)
botao_emprestar.pack(pady=5)
botao_devolver.pack(pady=5)
label_status.pack(side=tk.BOTTOM, fill=tk.X)

# 4. Inicia o loop principal do programa (deixa a janela visível e interativa)
janela.mainloop()