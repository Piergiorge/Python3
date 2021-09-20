# pega 3 inteiros, caso sejam iguais, retorna a soma x 3. Caso não sejam, retorna apenas a soma
num1 = int(input ('Digite um número: '))
num2 = int(input ('Digite um número: '))
num3 = int(input ('Digite um número: '))

def soma(x,y,z):
    if num1 == num2 == num3:
        soma = (num1 + num2 + num3) * 3
        return soma
    else:
        soma = (num1 + num2 + num3)
        return soma

soma(num1,num2,num3)
