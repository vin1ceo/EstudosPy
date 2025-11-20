entrada = "100, 50, 200" #recebe a entrada
precos_texto = entrada.split (',') # reparte cada preço sobre a virgula
precos_desconto = []

for preco in precos_texto:
    valor_float = float(preco)
    novo_valor = valor_float * 0.9
    precos_desconto.append(novo_valor)

print(precos_desconto)


