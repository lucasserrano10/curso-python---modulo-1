print(f'-=-'*20)
print('10 TERMOS PA')
print(f'-=-'*20)
a1 = int(input('PRIMEIRO TERMO :'))
razao = int(input('QUAL A RAZÃO : '))
termo = a1
c = 1
while c <= 10:
    print(termo)
    termo += razao
    c += 1
print(f'fim')