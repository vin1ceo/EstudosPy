from datetime import date, time, timedelta, datetime



## Representar a data atual.
agora = datetime.now()
print(f"A data de hoje é {agora}")



##Representar a data de hoje
hoje = datetime.today()
print(f"{hoje}")


## Representar uma data
natal = datetime(year=2025, month=12,day=25, minute=0, second=0)

print(f"Natal 2025 é: {natal}")

## Formatação de data e hora com a strftime.
print(natal.strftime("O natal será no dia %d/%m/%Y, ás %H:%H."))


## Converter uma str para data e hora.
texto_da_data = "06/10/2025 20:30"
data_convertida = datetime.strptime(texto_da_data, "%d/%m/%Y %H:%M")
print(f"Objeto datetime convertido: {data_convertida}")


## fazer calculos com timedelta.
agora = datetime.now()

uma_semana_e_meia = timedelta(days=7, hours=12)

data_futura = agora + uma_semana_e_meia
print(f"Daqui a 1 semana e 12h será: {data_futura.strftime('%d/%m/%Y %H:%M')}")

diferenca = data_futura - agora
print(f"A diferença entre as duas datas é de {diferenca.days} dias e {diferenca.seconds // 3600} horas.")


