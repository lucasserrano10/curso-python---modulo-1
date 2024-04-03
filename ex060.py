qtdadeNumeros = 0
somaValores = 0
maior = 0
menor = 10000000000000000000000
resp = 'S'
while resp == 'S':
    num = int(input('DIGITE UM NÚMERO :'))
    qtdadeNumeros += 1
    somaValores += num
    if qtdadeNumeros == 1:
        maior == menor == num
    if num >= maior:
        maior = num
    if num <= menor:
        menor = num
    resp = str(input('QUER CONTINUAR [S/N] : ')).upper().strip()
media = (somaValores/qtdadeNumeros)
print(f'-'*20)
print(f'VOCE DIGITOU {qtdadeNumeros} NÚMEROS')
print(f'-'*20)
print(f'A MÉDIA DOS VALORES É {media}')
print(f'-'*20)
print(f'MAIOR NÚMERO DIGITADO FOI {maior}')
print(f'-'*20)
print(f'MENOR NÚMERO DIGITADO FOI {menor}')

print('ACABOU')