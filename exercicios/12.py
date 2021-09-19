# retorna o calendario de um determinado mes e ano
import calendar  
ano = int(input("Digite o ano (formato xxxx): "))  
mes = int(input("Qual o mês (formato xx): "))  
def calendario(mes,ano):
    print (calendar.month(ano,mes))
    
calendario(mes, ano)
