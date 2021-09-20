# carrega um inteiro, verifica a diferenca em relacao a 17, verifica se essa diferença é maior do que 17 e retorna duas vezes o valor absoluto
num = int(input ('Digite um número: '))
diferenca = num - 17
if (diferenca > 17):
    print (abs(diferenca)*2)
