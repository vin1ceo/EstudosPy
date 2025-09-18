#BIBLIOTECA QUE POSSUI FUNÇÕES RELACIONADAS A TEMPO##
import time
## ------------------------------------------- ##
## Mensagem inicial do sistema ##
print("Iniciando contagem regressiva...")
##--------------------------------------------
## Em um range de 10 segundos regressivos o sistema vai printar o numero em um intervalo de 1 segundo.
# Ao final o sistema vai apresentar FOGO!
for numero in range(10,-1 ,-1):
    print(numero)
    time.sleep(1)

print("Fogo!!")