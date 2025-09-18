
## DEF são as funções da calculadora 
def adicao(n1,n2):
    return n1 + n2

def multiplicacao(n1,n2):
    return n1 * n2

def subtracao(n1,n2):
    return n1 - n2

def divisao(n1,n2):
    if n2 == 0:
        return "Erro: Divisão por 0!"
    else:
        n1 / n2

## While é um looping infinito até que determinada ação seja executada e parar para começar outra condição.
while True:
    print("Calculadora Digital")
    print("Operações disponíveis: +, -, *, /")
    print("Digite 'sair' a qualquer momento para encerrar.")

    n1_input = input("Digite o primeiro número: ")
    if n1_input == 'sair':
        break

    operacao = input("Digite a operação matemática: ")
    if operacao == 'sair':
        break
    
    n2_input = input("Digite o segundo número: ")
    if n2_input == 'sair':
        break
##------------------------------------------------------------------

# Conversor de string para número
    n1 = float(n1_input)
    n2 = float(n2_input)

    ## backend
    # a declaracao da variavel resultado nesse contexto é para idealizar ela no código, para que não retorne erros no final da operação
    #condicional
    resultado = 0
    if operacao == '+':
        resultado = adicao(n1,n2)
    elif operacao == '*':
        resultado = multiplicacao(n1,n2)
    elif operacao == '-':
        resultado = subtracao(n1,n2)
    elif operacao == '/':
        resultado = divisao(n1,n2)
    else:
        resultado = "Operação inválida"
    
    ## Aqui o programa vai apresentar o resultado final proposto da calculadora.
    print("---------------------")
    print(f"{n1} {operacao} {n2} = {resultado}")