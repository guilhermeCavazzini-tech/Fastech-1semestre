vetor = []
x = 1
multiplicacao = 1
soma = 0

for x in range(5):
    vetor.append(int(input('insira os numeros: ')))

for v in vetor:
    soma += v
    multiplicacao *= v

print('-__-'*32)
print(vetor)
print('-__-'*32)
print('a soma desses numeros são:', soma)
print('-__-'*32)
print('a multiplicação desses numeros é:', multiplicacao)
