# 14) Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses
# três argumentos.

def exercicio_14(a, b, c):
    s = a + b + c
    return s


print('SOMA DE TRÊS NÚMEROS')
a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))

print('Soma = ', exercicio_14(a, b, c))
