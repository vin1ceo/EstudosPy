entrada = "python código vinicius"
palavras = entrada.split()
hashtags = []

for palavra in palavras:

    tag_pronta = '#' + palavra.upper()
    hashtags.append(tag_pronta)

print(hashtags)