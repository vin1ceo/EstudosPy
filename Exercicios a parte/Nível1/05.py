## DEF é a função, com ela se pode utilizar em todo o software que for utilizar.
def calcular_media(n1, n2, n3):
    soma = n1 + n2 + n3
    media = soma / 3
    return media
## ---------------------------------------------------------------------------------##

## float é o tipo de valor dentro desta grade existem outras formas, dependendo do contexto como = int, decimal)
numero1 = float(input("Digite a primeira nota: "))
numero2 = float(input("Digite a segunda nota: "))
numero3 = float(input("Digite a terceira nota: "))
## --------------------------------------------------------------------------------##

## Aqui vemos uma váriavel nova onde está puxando a nossa função DEF, com os números que o usuário inputou, forma de chamar a função.
media_calculada = calcular_media(numero1, numero2, numero3)
## --------------------------------------------------------------##

## A famosa estrutura condicional, neste exemplo traz SE a média_calculada for maior ou igual a 7, o sistema irá exibir aluno aprovado
#caso contrário não aprovado.
if media_calculada >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado :c ")
## ---------------------------------##

# apresentação final #
print (f"A sua média é: {media_calculada:.1f}")