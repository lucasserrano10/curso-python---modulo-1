a = int(input('ESCREVA UM NÚMERO PARA SABER A SEQUÊNCIA DE FIBONACCI :'))
contador = 0
b = 1
while contador < 9:
    c = a + b
    print(c)
    a = b
    b = c
    c = a + b
    contador+=1
