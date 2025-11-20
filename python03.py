numeros = "10,20,30".split(',')
resultado = []

for n in numeros:
    soma = int(n) + 5  # O erro vai acontecer aqui!
    resultado.append(soma)

print(resultado)
