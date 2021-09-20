#verifica se a string comeca com um determinado padrão
a = input("Escreva a string: ")
b = input("Escreva o padrão: ")
if a.startswith(b):
    print(a)
else:
    a = b + a
    print(a)
