# Conta quantas vezes 1 determinado termo aparece na lista
frutas = ['banana', 'laranja','goiaba', 'banana']
termo = input("Digite o termo de busca: ")
x = frutas.count(termo)
if x != 0:
    print (f'Existem {x} ocorrências do termo ({termo}) na lista')
