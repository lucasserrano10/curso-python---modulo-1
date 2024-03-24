num1 = float(input('DIGITE O PRIMEIRO VALOR :'))
num2 = float(input('DIGITE O SEGUNDO VALOR:'))
num3 = float(input('DIGITE O TERCEIRO VALOR:'))
menor = num1

if num2 < num1 and num2 < num3:
    num2 = menor
if num3 < num2 and num3 < num1:
    num3 = menor

maior = num1

if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num2 and num3 > num1:
    maior = num3

print(f'maior número digitado {maior}')
print(f'menor numero digitado {menor}')

