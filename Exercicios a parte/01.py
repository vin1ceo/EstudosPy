print("-----------tabuada------------")

numero_usuario = int(input("Digite um número: "))

for multiplicador in range(1,11):
    resultado = numero_usuario * multiplicador
    print(f"{numero_usuario} x {multiplicador} = {resultado}")