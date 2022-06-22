#7) Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário
#de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o
#usuário pode digitar letras maiúsculas ou minúsculas.

nome = input('Insira seu nome aqui: ')
nome = nome.upper()
print('-_____-' * 32)
print('seu nome em maiusculo de trás para frente é:', (nome[::-1]))
