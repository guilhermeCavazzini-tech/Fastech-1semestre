#9) Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato
#de escada.

name = input("Digite seu nome:")
print(*input("Digite seu nome novamente: "), sep="\n")
v = len(name) + 1
for l in range(v):
    print(name[:l])
