primeiro_vetor = []
segundo_vetor = []
terceiro_vetor = []

for p in range(10):
    primeiro_vetor.append(input("Digite o elemento da " + str(p + 1) + "ª posição do primeiro vetor: "))
print('-______-'*32)
for p in range(10):
    segundo_vetor.append(input("Digite o elemento da " + str(p + 1) + "ª posição do segundo vetor: "))
print('-______-'*32)
for l in range(10):
    terceiro_vetor.append(primeiro_vetor[l])
    terceiro_vetor.append(segundo_vetor[l])
print('-______-'*32)
print(terceiro_vetor)
