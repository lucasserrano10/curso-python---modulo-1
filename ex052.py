somaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
mulheresMenor = 0
for c in range(1,5):
    print(f'---{c}-PESSOA ---')
    nome = input('NOME :').strip()
    idade = int(input('idade :'))
    sexo = input('SEXO [M/F] :').strip().upper()
    somaIdade += idade
    if c == 1 and sexo == 'M':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo == 'M' and idade > maiorIdadeHomem:
        maiorIdadeHomem == idade
        nomeVelho = nome
    if sexo == 'F' and idade < 20:
        mulheresMenor += 1

media = somaIdade / 4
print(f'A MÉDIA DA IDADE DO GRUPO É {media}')
print(f'O HOMEM MAIS VELHO TEM {maiorIdadeHomem} ANOS E SE CHAMA {nomeVelho}')
print(f'EXISTEM {mulheresMenor} MULHERES COM MENOS DE 20 ANOS')