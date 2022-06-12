idade = []
altura = []
a = 0

for a in range(5):
    print('-_____-' * 32)
    print(a + 1, '° Pessoa')
    altura.append(float(input("Qual é a altura da pessoa? ")))
    idade.append(int(input('Qual é a idade da pessoa? ')))

print('idade normal', idade)
print('idade invertida', (idade[::-1]))

print('-_____-' * 32)

print('altura normal', altura)
print('altura invertida', (altura[::-1]))
