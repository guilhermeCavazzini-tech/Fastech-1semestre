#4) Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos
#quadrados dos elementos do vetor.

n = []
quadrado = []
m = 0

for x in range(3):
     n.append(int(input("Digite um número inteiro: ")))
for i in n:
    m = m + n[x] ** 2
    quadrado.append(m)

print('Esse são os numeros que voce ultilizou', n)
print('A soma de todos esses número elevados ao quadrado é: ', m)