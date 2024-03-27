from time import sleep

print('ÁREA DE NOTAS DO ALUNO')
print('Seja Bem Vindo !')

print(f'-=-=' * 20)

nome = str(input('NOME DO ALUNO :')).strip()

n1 = float(input('NOTA DO PRIMEIRO TRIMESTRE :'))
n2 = float(input('NOTA DO SEGUNDO TRIMESTRE :'))
n3 = float(input('NOTA DO TERCEIRO TRIMESTRE :'))

print(f'-=-=' * 20)
print('analisando...')
sleep(5)
print(f'-=-=' * 20)

media = (n1+n2+n3)/3

if media >= 7:
    print(f'APROVADO, PARABÉNS, {nome}')
    print(f'MÉDIA FINAL, {media}')
    print(f'-=-=' * 20)
elif 5 < media <= 6.9:
    print('RECUPERAÇÃO')
    print(f'MÉDIA FINAL, {media}')
    print(f'-=-=' * 20)
else:
    print('RETIDO')
    print(f'MÉDIA FINAL, {media}')
    print(f'-=-=' * 20)
