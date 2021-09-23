import requests
# GET
requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
#print (requisicao)
x = requisicao.json()
print ('#' * 50)
for i in x:
    for j in x[i]:
        print(f'{i}:\t{j}\t{x[i][j]}')
print ('#' * 50)
