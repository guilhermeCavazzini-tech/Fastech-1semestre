def exercicio_17(a, b):
    if a > 20:
        a = 20
    if b > 20:
        b = 20
    print('-+-' * a)
    c = 0
    while c < a:
        z = '|'
        print(f'{z}{z:>{(a * 3 - 1)}}')
        c += 1
    print('-+-' * a)


a = int(input('largura:'))
b = int(input('altura:'))
exercicio_17(a, b)
