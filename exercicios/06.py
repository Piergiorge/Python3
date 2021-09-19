# cria uma lista e tupla a partir de um conjunto de valores separados por vírgula
lista = (input ("Digite os valores: "))
lista = lista.split(sep=",")
print (list(lista))
print (tuple(lista))
