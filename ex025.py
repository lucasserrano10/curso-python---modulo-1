import random
from time import sleep
numeros = [0,1,2,3,4,5]
computadorNum = random.choice(numeros)
print(f'O COMPUTADOR PENSOU NESSE NUMERO {computadorNum}')

usuarioNumero = int(input('ESCREVA UM NÚMERO DE 0 A 5 :'))
print('processando...')

sleep(4)

if usuarioNumero != computadorNum:
    print('SEU NÚMERO É DIFERENTE DO QUE O DO COMPUTADOR !')
else:
    print('VOCÊ PENSOU NO MESMO NÚMERO DO COMPUTADOR')