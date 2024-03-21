n1 = int(input('DIGITE UM NÚMERO : '))
print(f'sucessor : {n1+1}')
print(f'antecessor : {n1-1}')

print('-----------OUTRO EXERCÍCIO-------------------')

nota1 = float(input('DIGITE A NOTA DO PRIMEIRO TRIMESTRE :'))
nota2 = float(input('DIGITE A NOTA DO SEGUNDO TRIMESTRE :'))
nota3 = float(input('DIGITE A NOTA DO TERCEIRO TRIMESTRE :'))

media = (nota1 + nota2 + nota3)/3
print(f'A MÉDIA DO ALUNO É {media}')

print('-----------OUTRO EXERCÍCIO-------------------')

salarioPre = float(input('DIGITE SEU SALÁRIO ATUAL :'))
print('PARABÉNS, VOCÊ FOI PROMOVIDO !')
perguntaUsuario = int(input('quer saber o novo salário ? digite 1, se não digite 2'))

if perguntaUsuario == 1:
    print('VOCÊ RECEBEU UM AUMENTO DE 15% !')
    print(f'SEU NOVO SALÁRIO É {salarioPre*1.15}')
else:
    print("PROGRAMA ENCERRADO !")

print('-----------OUTRO EXERCÍCIO-------------------')

km = float(input('QUAL FOI A QUANTIDADE DE KM RODADO PELO CARRO ? :'))
dias = int(input('QUANTOS DIAS ELE FICOU ALUGADO ? :'))
totaldias = dias * 60
totalkms = km * 0.15
print(f'O VALOR PAGO SERÁ {totaldias}R$ PELOS DIAS ALUGADOS, E {totalkms}R$ PELA QUILOMETRAGEM, TOTALIZANDO {totalkms + totaldias}R$')


