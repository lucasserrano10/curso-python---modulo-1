print(f'-=-'*20)
print('10 TERMOS PA')
print(f'-=-'*20)
a1 = int(input('PRIMEIRO TERMO :'))
razao = int(input('QUAL A RAZÃO : '))
termo = a1
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(termo)
        termo += razao
        c+=1
    print('pausa')
    mais = int(input('QUANTOS VOCÊ QUER MOSTRAR A MAIS ?'))
print('FIM')