contadorHomens = 0
mulherMenosVinte = 0
pessoasAdultas = 0 #maior de 18 anos#
resp = "S"
while resp == "S":
    print(f'=' * 30)
    print(f'CADASTRO DE PESSOAS ')
    print(f'=' * 30)
    idade = int(input('SUA IDADE :'))
    if idade > 18:
        pessoasAdultas += 1
    sexo = str(input('SEXO [F/M] :')).strip().upper()
    if sexo == "M":
        contadorHomens += 1
    elif idade < 20 and sexo == "F":
        mulherMenosVinte +=1
    resp = str(input('DESEJA CONTINUAR ? [S/N]:')).strip().upper()
    if resp == "N":
        break
print(f'QUANTIDADE DE HOMENS : {contadorHomens}')
print(f'QUANTIDADE DE MULHERES COM MENOS DE 20 ANOS : {mulherMenosVinte}')
print(f'QUANTIDADE DE MAIORES DE IDADE : {pessoasAdultas}')