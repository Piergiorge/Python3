# dias de vida
from datetime import date
# qual o dia que vc nasceu?
dia = int(input ('Digite o dia do seu nascimento: '))
mes = int(input ('Digite o mes do seu nascimento: '))
ano = int(input ('Digite o ano do seu nascimento: '))

data1 = date(ano, mes, dia)
data_hoje = date.today()
data2 = date(data_hoje.year, data_hoje.month, data_hoje.day)
val = data2 - data1
print(f'Você está vivo há {val.days} dias')
