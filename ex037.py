print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('QUERIDO CANDIDATO, VAMOS VER SUA CATEGORIA')
print(f'-=-=' * 20)

nome = str(input('DIGITE SEU NOME:'))
print(f'-=-=' * 20)
anoNascimento = int(input('ANO DE NASCIMENTO: '))

calculoIdade = 2024 - anoNascimento

if calculoIdade <= 9:
    print(f'{nome} - CATEGORIA MIRIM')
elif 9 > calculoIdade <= 14:
    print(f'{nome} - CATEGORIA INFÂNTIL')
elif 14 > calculoIdade <= 19:
    print(f'{nome} - CATEGORIA JÚNIOR')
elif 19 > calculoIdade <= 21:
    print(f'{nome} - CATEGORIA SÊNIOR')
else:
    print(f'{nome}, - CATEGORIA MASTER')
