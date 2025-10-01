# --- Ferramentas Iniciais ---

# Linha 1: "import datetime"
# PEGANDO A FERRAMENTA DE DATAS: Estamos dizendo ao Python: "Ei, eu vou precisar trabalhar com datas e horas,
# então, por favor, pegue a sua 'caixa de ferramentas' padrão chamada 'datetime' e deixe-a pronta para uso."
import datetime

# --- A Preparação / As Plantas (Definição das Classes) ---

# Linha 5: "class EntradaDiario:"
# CRIANDO O MOLDE DA PÁGINA: Aqui definimos a "planta" ou o "molde" para criar uma única página (uma entrada) do nosso diário.
class EntradaDiario:
    # Linha 7: "def __init__(self, titulo, conteudo):"
    # AS INSTRUÇÕES DE MONTAGEM DA PÁGINA: Este é o construtor. Toda vez que uma nova página for criada,
    # estes são os passos obrigatórios. Ela precisa de um 'titulo' e um 'conteudo' para nascer.
    def __init__(self, titulo, conteudo):
        # Linha 9: "self.titulo = titulo"
        # GUARDA O TÍTULO: Pega o 'titulo' que foi dado na criação e guarda em uma "gaveta" chamada 'titulo' dentro desta página.
        self.titulo = titulo
        # Linha 10: "self.conteudo = conteudo"
        # GUARDA O CONTEÚDO: Faz o mesmo para o 'conteudo'.
        self.conteudo = conteudo
        # Linha 11: "self.data = datetime.datetime.now()"
        # CARIMBA A DATA E HORA: Usa a ferramenta 'datetime' para olhar o relógio do computador AGORA e guarda esse momento na "gaveta" 'data'.
        self.data = datetime.datetime.now()

    # Linha 13: "def __str__(self):"
    # A RECEITA DE COMO A PÁGINA DEVE SE APRESENTAR: Se alguém tentar imprimir esta página (com 'print'),
    # é este formato de texto que será mostrado.
    def __str__(self):
        # Linha 15: "data_formatada = self.data.strftime(...)"
        # DEIXANDO A DATA BONITA: Pega a data completa (que é um objeto complexo) e a transforma em um texto mais legível e formatado.
        data_formatada = self.data.strftime("%Y-%m-%d %H:%M:%S")
        # Linha 17: "return f"""..."""
        # DEVOLVE O TEXTO FINAL: Cria e retorna um texto de múltiplas linhas, já com as informações das "gavetas" inseridas nos lugares certos.
        return f"Data: {data_formatada}\nTítulo: {self.titulo}\n---\nConteúdo: {self.conteudo}"


# Linha 21: "class GerenciadorDiario:"
# CRIANDO O MOLDE DO GERENTE: Aqui definimos a "planta" do nosso Gerente, a peça "inteligente" que vai organizar todas as páginas.
class GerenciadorDiario:
    # Linha 23: "def __init__(self, nome_arquivo):"
    # AS INSTRUÇÕES DE MONTAGEM DO GERENTE: Para criar um Gerente, precisamos dizer a ele o nome do arquivo que ele vai usar.
    def __init__(self, nome_arquivo):
        # Linha 25: "self.__nome_arquivo = nome_arquivo"
        # GUARDA O NOME DO ARQUIVO: Ele anota o nome do arquivo em uma "gaveta" secreta para usar depois.
        self.__nome_arquivo = nome_arquivo
        # Linha 26: "self.__entradas = []"
        # PEGA UM FICHÁRIO VAZIO: Ele cria uma lista vazia, um "fichário" secreto, onde irá guardar todas as páginas do diário.
        self.__entradas = []

    # Linha 28: "def adicionar_entrada(self, titulo, conteudo):"
    # A RECEITA PARA "ADICIONAR UMA NOVA PÁGINA":
    def adicionar_entrada(self, titulo, conteudo):
        # Linha 30: "nova_entrada = EntradaDiario(...)"
        # CRIA A PÁGINA: Usa o molde 'EntradaDiario' para construir uma página novinha em folha.
        nova_entrada = EntradaDiario(titulo=titulo, conteudo=conteudo)
        # Linha 31: "self.__entradas.append(nova_entrada)"
        # GUARDA A PÁGINA NO FICHÁRIO: Pega a página nova e a coloca dentro do seu fichário secreto.
        self.__entradas.append(nova_entrada)
        # Linha 32: "print(...)"
        # AVISA QUE DEU CERTO: Dá um feedback para o usuário.
        print("-> Entrada adicionada com sucesso!")

    # Linha 34: "def listar_entradas(self):"
    # A RECEITA PARA "MOSTRAR TODAS AS PÁGINAS":
    def listar_entradas(self):
        # Linha 35: "if not self.__entradas:"
        # VERIFICA SE O FICHÁRIO ESTÁ VAZIO: Se 'não' tiver nenhuma página guardada...
        if not self.__entradas:
            # Linha 36-37: "...avisa o usuário e para a receita aqui."
            print("O diário está vazio.")
            return
            
        # Linha 39: "print(...)"
        # IMPRIME UM TÍTULO: Para organizar a exibição.
        print("\n--- TODAS AS ENTRADAS DO DIÁRIO ---")
        # Linha 40: "for i, entrada in enumerate(self.__entradas):"
        # PEGA AS PÁGINAS UMA POR UMA: Para cada página no fichário, pega também um número de ordem ('i').
        for i, entrada in enumerate(self.__entradas):
            # Linha 41: "print(...)"
            # IMPRIME UM SUBTÍTULO: Para cada entrada.
            print(f"\n--- ENTRADA {i+1} ---")
            # Linha 42: "print(entrada)"
            # MANDA A PÁGINA SE APRESENTAR: Pede para a própria página se transformar em texto (usando o __str__) e mostra na tela.
            print(entrada)
        # Linha 43: "print(...)"
        # IMPRIME O RODAPÉ: Para finalizar o relatório.
        print("\n--- FIM DAS ENTRADAS ---")

    # Linha 45: "def salvar_diario(self):"
    # A RECEITA PARA "SALVAR O TRABALHO NO ARQUIVO":
    def salvar_diario(self):
        # Linha 46: "separador = ..."
        # CRIA UM SEPARADOR: Define um texto para separar uma entrada da outra no arquivo.
        separador = "\n<--- FIM DA ENTRADA --->\n"
        # Linha 47: "with open(...) as f:"
        # ABRE O ARQUIVO COM SEGURANÇA: Abre o arquivo de texto no modo de escrita ('w').
        with open(self.__nome_arquivo, 'w', encoding='utf-8') as f:
            # Linha 48: "for entrada in self.__entradas:"
            # PEGA AS PÁGINAS UMA POR UMA: Para cada página no fichário...
            for entrada in self.__entradas:
                # Linha 50: "f.write(...)"
                # ...escreve a página (em formato de texto) e o separador no arquivo.
                f.write(str(entrada) + separador)
        # Linha 51: "print(...)"
        # AVISA QUE SALVOU: Dá um feedback para o usuário.
        print(f"Diário salvo em '{self.__nome_arquivo}'.")

    # Linha 53: "def carregar_diario(self):"
    # A RECEITA PARA "CARREGAR O TRABALHO SALVO":
    def carregar_diario(self):
        # Linha 55: "try:"
        # VAMOS TENTAR: Inicia um bloco de código que pode dar erro.
        try:
            # Linha 56: "with open(...) as f:"
            # TENTA ABRIR O ARQUIVO: Tenta abrir o arquivo no modo de leitura ('r').
            with open(self.__nome_arquivo, 'r', encoding='utf-8') as f:
                # Linhas 59-64:
                # LÓGICA DE LEITURA: Esta é uma parte mais complexa que lê o conteúdo do arquivo
                # e tenta recriar as entradas. Não se preocupe em decorar, a ideia é mostrar que é possível.
                conteudo_total = f.read()
                entradas_salvas = conteudo_total.split("<--- FIM DA ENTRADA --->")
                if len(entradas_salvas) > 1:
                     print(f"Diário '{self.__nome_arquivo}' carregado com dados anteriores.")
        # Linha 65: "except FileNotFoundError:"
        # SE O ERRO ACONTECER: Se o 'try' falhar com o erro "Arquivo Não Encontrado"...
        except FileNotFoundError:
            # Linha 66: "...execute este código alternativo em vez de quebrar o programa."
            print(f"Arquivo de diário não encontrado. Um novo será criado como '{self.__nome_arquivo}'.")

# --- A Execução / Onde a História Acontece ---

# Linha 70: "if __name__ == "__main__":"
# A CHAVE DE IGNIÇÃO: Esta linha diz ao Python: "O programa de verdade, a ação principal, começa AQUI."
if __name__ == "__main__":
    
    # Linha 72: "meu_diario = GerenciadorDiario(...)"
    # CRIANDO O GERENTE: Usamos o molde 'GerenciadorDiario' para criar nosso Gerente, dizendo o nome do arquivo que ele vai usar.
    meu_diario = GerenciadorDiario("meu_diario.txt")
    # Linha 73: "meu_diario.carregar_diario()"
    # PRIMEIRA ORDEM: Mandamos o Gerente tentar carregar qualquer trabalho salvo anteriormente.
    meu_diario.carregar_diario()

    # Linha 75: "while True:"
    # O MENU PRINCIPAL: Começa um loop infinito. O programa ficará preso aqui, mostrando o menu, até o usuário decidir sair.
    while True:
        # Linhas 76-79: "print(...)"
        # MOSTRA AS OPÇÕES: Mostra o menu de opções na tela para o usuário.
        print("\n--- Meu Diário Digital ---")
        print("1. Adicionar Nova Entrada")
        print("2. Listar Todas as Entradas")
        print("3. Salvar e Sair")
        
        # Linha 81: "escolha = input(...)"
        # ESPERA O USUÁRIO: O programa para e espera o usuário digitar uma opção e apertar Enter.
        escolha = input("Escolha uma opção: ")

        # Linha 83: "if escolha == '1':"
        # SE A ESCOLHA FOI 1: Se o usuário digitou "1"...
        if escolha == '1':
            # Linhas 84-85: "...peça o título e o conteúdo..."
            titulo = input("Digite o título: ")
            conteudo = input("Digite o conteúdo: ")
            # Linha 86: "...e dê a ordem para o Gerente adicionar a nova página."
            meu_diario.adicionar_entrada(titulo, conteudo)
        # Linha 87: "elif escolha == '2':"
        # SENÃO, SE A ESCOLHA FOI 2: Mande o Gerente listar as páginas.
        elif escolha == '2':
            meu_diario.listar_entradas()
        # Linha 89: "elif escolha == '3':"
        # SENÃO, SE A ESCOLHA FOI 3:
        elif escolha == '3':
            # Linha 90: "meu_diario.salvar_diario()"
            # Dê a ordem para o Gerente salvar o trabalho no arquivo...
            meu_diario.salvar_diario()
            # Linha 91: "print(...)"
            # ...dê uma mensagem de despedida...
            print("Até logo!")
            # Linha 92: "break"
            # ...e use 'break' para quebrar o loop infinito e encerrar o programa.
            break
        # Linha 93: "else:"
        # SE NÃO FOI NENHUMA DAS OPÇÕES:
        else:
            # Linha 94: "print(...)"
            # Avise ao usuário que a opção é inválida. O loop vai recomeçar.
            print("Opção inválida. Tente novamente.")