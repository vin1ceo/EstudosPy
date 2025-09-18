def calcular_media(n1, n2, n3):
    soma = n1 + n2 + n3
    media = soma / 3
    return media

numero1 = float(input("Digite a primeira nota: "))
numero2 = float(input("Digite a segunda nota: "))
numero3 = float(input("Digite a terceira nota: "))

media_calculada = calcular_media(numero1, numero2, numero3)

print (f"A sua média é: {media_calculada:.1f}")
