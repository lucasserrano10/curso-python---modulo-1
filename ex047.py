print(f'-=-'*20)
print('10 TERMOS PA')
print(f'-=-'*20)
a1 = int(input('PRIMEIRO TERMO :'))
razao = int(input('QUAL A RAZÃO : '))
a10 = a1 + (10-1)*razao
for c in range(a1,a10 + razao,razao):
    print(c)
print('acabou !')
