def dizeroi(nome):
    return f"Oi {nome}"
    

def incentivar(nome):
    return f"Olá {nome}! Vamos aprender python."

def mensagem_pvini(funcaomsg):
    return funcaomsg("Vinicius")

mensagem_pvini(dizeroi)
mensagem_pvini(incentivar)

print(dizeroi)
print(incentivar)