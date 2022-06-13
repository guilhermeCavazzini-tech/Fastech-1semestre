name = input("Digite seu nome:")
print(*input("Digite seu nome novamente: "), sep="\n")
v = len(name) + 1
for l in range(v):
    print(name[:l])
