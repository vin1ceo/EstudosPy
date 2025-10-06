from datetime import date, time, timedelta, datetime


aniversario = datetime(year=2025,month=10,day=21, hour=20, minute=1,second=0)

print(f"O aniversário de Vinicius é: {aniversario}")

print(aniversario.strftime("O aniversário será: %d/%m/%Y, ás %H:%H."))

print(aniversario.strftime("O anivérsario será no mês de: %d de %B, %Y"))
