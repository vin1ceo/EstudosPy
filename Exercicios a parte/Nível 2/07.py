

## aqui o usuário inseriu o número que em tese seria o número de que irá ser multiplicado.
numero_usuario = int(input("Digite o número: "))
##----------------------------------------------------

# Sistema printa na tela para 
print(f"---- Tabuada do {numero_usuario} ----")

for multiplicador in range(1,11):
    resultado = numero_usuario * multiplicador
    print(f"{numero_usuario} x {multiplicador} = {resultado}")
