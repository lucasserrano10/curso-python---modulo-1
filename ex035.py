print('BEM VINDO AO PROGRAMA DE ALISTAMENTO MILITAR !')
print('VAMOS VERIFICAR SUA SITUAÇÃO !')

print(f'-=-='*20)

anoNascimento = int(input('DIGITE SEU ANO DE NASCIMENTO: '))

calculoIdade = 2024 - anoNascimento
calculoTempoFalta = 18 - calculoIdade

if calculoIdade == 18:
    print('NOTÍCIA BOA !, É HORA DE SE ALISTAR')
    print(f'-=-=' * 20)
elif calculoIdade > 18:
    print('FASE DE ALISTAMENTO JA SE PASSOU, PERDEU !')
    print(f'-=-=' * 20)
else:
    print(f'AINDA VOCÊ TEM TEMPO GAROTO, FALTAM {calculoTempoFalta} ano(s)')
    print(f'-=-=' * 20)