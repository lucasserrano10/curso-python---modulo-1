soma = 0
cont = 0
for c in range(1,500,2):
    if c % 3 == 0:
        print(c)
        cont += 1
        soma += c
print(f' a soma de todos os números de 1 a 500, que são {cont} divisiveis por 3 é igual :{soma}')
