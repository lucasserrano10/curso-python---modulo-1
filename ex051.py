
maiorPeso = 0
menorPeso = 0
for c in range(1,6):
    peso = float(input(f'DIGITE O PESO DA {c}* PESSOA :'))
    if c == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
print(f'O MENOR PESO FOI {menorPeso}')
print(f'O MAIOR PESO FOI {maiorPeso}')
