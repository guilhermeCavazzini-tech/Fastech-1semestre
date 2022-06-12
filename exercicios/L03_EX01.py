aprovados = []
notas = 0
alunos = 1

for h in range(1):
    for g in range(10):
        print('Insira a nota do', alunos, '° aluno')
        notas = int(input('insira a 1° nota: ')) + int(input('insira a 2° nota: ')) + int(
            input('insira a 3° nota: ')) + int(input("insira a 4° nota: "))
        if notas / 4 >= 7:
            aprovados.append(+1)
            alunos = alunos + 1

print(len(aprovados), 'alunos foram aprovados')