def conversor_un(n1):
    conversor = n1 * 100
    return conversor

numero1 = float(input("Digite o valor em metros:"))

convertido = conversor_un(numero1)

print(f"{numero1} metros equivalem a {convertido:.2f} centímetros.")