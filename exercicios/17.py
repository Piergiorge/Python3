# soma de numeros inteiros

num1 = int(input ('Digite um número: '))
num2 = int(input ('Digite um número: '))
num3 = int(input ('Digite um número: '))
soma = (num1 + num2 + num3)
soma_list = list(str(soma))
if len(soma_list) == 1:
    print (f'A soma resultou em um valor com apenas 1 dígito ({soma})!')
elif len(soma_list) > 1:
    valor = 0
    for i in soma_list:
        valor = int(i) + valor
    print (f'A soma apresentou pelo menos 2 dígitos ({soma}) que, ao serem somados, resultaram em {valor}')
