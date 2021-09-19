# recupera documentacao para as funções internas
import builtins
fun = input("Digite o nome da função: ")


def documentacao(i):
    internas = (dir(__builtins__))
    print (getattr(builtins, i)) if i in internas else print (f'Nenhuma documentação Python encontrada para {i}')
    if i in internas:
        print (i.__doc__)

documentacao(fun)
