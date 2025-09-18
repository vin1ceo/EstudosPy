##Biblioteca para gerar algo aleatório##
import random
###------------##
##------- váriavel que recebe um método da biblioteca random de um número aleatório inteiro entre 1 e 100 ---- #####
numero_secreto = random.randint(1,100)
##---------------------------------------------------------------------------------------------------------------------------------

## Titulo e enunciado do sistema ##
print("--- Jogo de Adivinhar o Número ---")
print("Eu pensei em um número entre 1 e 100. Tente adivinhar!")
#-------------------------------------------------------------------#

## Váriavel que recebe número inteiro, recebido pelo usuário que digitou##
numero_usuario = int(input("Adivinhe o número: "))
##---------------------------------------------------##

## Aqui vemos o WHILE que significa nesse contexto ENQUANTO = enquanto numero_usuario(variavel acima) for DIFERENTE do numero_secreto.
## IF = Se o numero do usuário for maior que o secreto, o sistema vai indicar que: Está muito alto, tente um número menor.
## Else =  # SENÃO (se não for igual nem maior, só pode ser menor), dá a dica "Muito Baixo"
# Dentro do loop inserimos novamente a variavel para que o usuário insira outro número.
# E quanto ele acertar o loop se encerra e aparece uma mensagem dizendo que acertou.
while numero_usuario != numero_secreto:
    if numero_usuario > numero_secreto:
        print("Muito Alto! tente um número menor")
    else:
        numero_usuario < numero_secreto
        print("Digite um número maior, muito baixo!")

    numero_usuario = int(input("Digite um novo número: "))

print(f"Parábens! Você acertou! O número correto é {numero_secreto}")

