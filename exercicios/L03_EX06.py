#6) Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe
#também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

lista = input('insira uma string: ').strip()
lista2 = input('insira uma string: ').strip()

print('-_____-'*32)

print('"', lista, '"' ' tem', len(lista), 'characters')

print('"', lista2, '"' ' tem', len(lista2), 'characters')

print('-_____-'*32)

if len(lista) != len(lista2):
    print("As duas strings são de tamanhos diferentes.")

if lista != lista2:
    print("As duas strings possuem conteúdos diferente")