from time import sleep
print(f'-=-'*30)
print('BANCO SERRANO')
print(f'-=-'*30)
valor = int(input('QUAL VALOR O SENHOR(a) DESEJA: R$'))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'TOTAL DE CÉDULAS {totalced} de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('NOTAS SAINDO PELA BOCA DO CAIXA !')
sleep(4)
print(f'-=-='*30)
print('OPERAÇÃO FINALIZADA')
print('VOLTE SEMPRE AO BANCO SERRANO !')
