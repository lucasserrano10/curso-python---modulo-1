n1 = int(input('NUMBER 1 :'))
n2 = int(input('NUMBER 2 :'))

if n1 > n2:
    print(f'o primeiro valor é maior, {n1}')
elif n2 > n1:
    print(f'o segundo valor é maior, {n2}')
else:
    print(f'ambos valores são iguais, {n1} e {n2}')