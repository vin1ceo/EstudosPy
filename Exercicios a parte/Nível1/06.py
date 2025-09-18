def numeromaior(n1,n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return n1
    
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

comparador = numeromaior(numero1, numero2)

print(f"Entre {numero1:.0f} e {numero2:.0f}, o maior é {comparador:.0f}!")
