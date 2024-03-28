somaMaior = 0
somaMenor = 0
cont =1

for c in range(1,9):
    anoNascimento = int(input(f'ANO DE NASCIMENTO DA PESSOA {cont} :'))
    if 2024 - anoNascimento >= 18:
        print(f'{c} - ATINGIU A MAIORIDADE')
        somaMaior += 1
        cont += 1
    else:
        print(f'{c} - NÃO ATINGIU A MAIORIDADE')
        somaMenor += 1
        cont += 1
print(f'PESSOAS MAIORES DE IDADE : {somaMaior}')
print(f'PESSOAS MENORES DE IDADE : {somaMenor}')
