# Linha 1: "import time"
# Estamos "pegando emprestado" um conjunto de ferramentas do Python para lidar com o tempo.
# Vamos usar uma dessas ferramentas para fazer uma pausa no nosso código.
import time

# --- Seção de Criação das "Plantas" ou "Moldes" (Classes) ---

# Linha 5: "class Instrumento:"
# Aqui criamos a "planta" MESTRA para qualquer instrumento. É uma ideia geral.
class Instrumento:
    # Linha 7: "def __init__(self, nome):"
    # Este é o "construtor". É uma lista de regras que devem ser seguidas toda vez que um novo instrumento é criado.
    # 'self' é a forma do objeto se referir a "eu mesmo". 'nome' é uma informação que ele DEVE receber.
    def __init__(self, nome):
        # Linha 9: "self.nome = nome"
        # A informação 'nome' que foi recebida é guardada dentro do próprio objeto, numa "etiqueta" chamada 'nome'.
        self.nome = nome
    
    # Linha 10: "def tocar(self):"
    # Definimos uma "habilidade" ou "ação" que todo instrumento deve ter.
    def tocar(self):
        # Linha 11: "print(f"Tocando {self.nome}...")"
        # A ação padrão é simplesmente dizer que está tocando.
        print(f"Tocando {self.nome}...")

# Linha 13: "class Violao(Instrumento):"
# Criamos a planta específica para um Violão. Dizemos que ele é um tipo de "Instrumento",
# então ele automaticamente herda tudo que a classe Instrumento tem.
class Violao(Instrumento):
    # Linha 15: "def __init__(self):"
    # As regras de construção específicas para o Violão.
    def __init__(self):
        # Linha 17: "super().__init__(nome="Violão")"
        # Aqui, ele chama o construtor da classe-mãe (Instrumento) e já avisa: "Olha, meu nome vai ser sempre 'Violão'".
        super().__init__(nome="Violão")
    
    # Linha 19: "def tocar(self):"
    # AQUI ESTÁ A MÁGICA DO POLIMORFISMO!
    # O Violão está "sobrescrevendo" a habilidade 'tocar'. Ele tem seu próprio jeito de fazer isso.
    def tocar(self):
        # Linha 21: "print(...)"
        # Em vez da mensagem genérica, ele imprime seu som característico.
        print("O Violão está reproduzindo o som das cordas: Trimm Trimm!")

# Linha 23: "class Bateria(Instrumento):"
# Fazemos exatamente o mesmo para a Bateria. É um Instrumento...
class Bateria(Instrumento):
    # Linha 25: "def __init__(self):"
    # ...com suas próprias regras de construção...
    def __init__(self):
        # Linha 27: "super().__init__(nome="Bateria")"
        # ...definindo seu nome...
        super().__init__(nome="Bateria")
    
    # Linha 29: "def tocar(self):"
    # ...e com seu próprio jeito de tocar.
    def tocar(self):
        # Linha 31: "print(...)"
        # Imprimindo o som único da bateria.
        print("A Bateria está fazendo: Tum ts Taaa")

# --- Seção da "Receita" ou "Ação" (Função) ---

# Linha 34: "def realizar_concerto(lista_de_instrumentos):"
# Criamos uma FUNÇÃO. Pense nela como uma receita de bolo, uma sequência de passos.
# Para essa receita funcionar, ela precisa de um ingrediente: uma "lista_de_instrumentos".
def realizar_concerto(lista_de_instrumentos):
    # Linha 36: "print(...)"
    # O primeiro passo da receita é imprimir uma mensagem na tela.
    print("\nO CONCERTO VAI COMEÇAR!")
    
    # Linha 38: "for i in range(5, 0, -1):"
    # Sua ideia da contagem regressiva! "Comece um loop, contando de 5 para baixo até 1".
    for i in range(5, 0, -1):
        # Linha 40: "print(i)"
        # Mostre o número atual da contagem.
        print(i)
        # Linha 41: "time.sleep(1)"
        # Use a ferramenta "time" que pegamos emprestado para fazer uma pausa de 1 segundo.
        time.sleep(1)
    
    # Linha 43: "print(...)"
    # Outro passo da receita: imprimir uma mensagem de início.
    print("QUE COMECEM OS SONS!")

    # Linha 45: "for instrumento in lista_de_instrumentos:"
    # O passo mais importante! "Para cada 'instrumento' dentro da lista que nos foi dada..."
    for instrumento in lista_de_instrumentos:
        # Linha 47: "instrumento.tocar()"
        # "...peça para esse 'instrumento' executar sua habilidade 'tocar()'."
        # A função não precisa saber se é um Violão ou uma Bateria. Ela só manda a ordem.
        # O próprio objeto sabe qual som fazer. ISSO É POLIMORFISMO!
        instrumento.tocar()

# --- Seção de Execução (Onde a Mágica Acontece) ---

# Linha 51: "violao_solo = Violao()"
# Usando a planta "Violao", estamos construindo um objeto violão de verdade e guardando na variável 'violao_solo'.
violao_solo = Violao()
# Linha 52: "bateria_rock = Bateria()"
# Usando a planta "Bateria", construímos uma bateria de verdade e guardamos na variável 'bateria_rock'.
bateria_rock = Bateria()
# Linha 53: "violao_base = Violao()"
# Podemos construir quantos objetos quisermos a partir da mesma planta.
violao_base = Violao()

# Linha 56: "minha_orquestra = [...]"
# Criamos a nossa lista de "ingredientes" para a receita: uma orquestra com os objetos que acabamos de construir.
minha_orquestra = [violao_solo, bateria_rock, violao_base]

# Linha 59: "realizar_concerto(minha_orquestra)"
# Finalmente, executamos a nossa receita ("realizar_concerto") e entregamos a ela a nossa orquestra para que ela possa trabalhar.
realizar_concerto(minha_orquestra)