import random
from time import sleep
numeros = [0,1,2,3,4,5]
computadorNum = random.choice(numeros)

usuarioNumero = int(input('ESCREVA UM NÚMERO DE 0 A 5 :'))
print('processando...')
print(f'-=-'*20)
sleep(3)
numeros = [0, 1, 2, 3, 4, 5]
c = 0
while usuarioNumero != computadorNum:
    computadorNum = random.choice(numeros)
    print('SEU NÚMERO É DIFERENTE DO QUE O DO COMPUTADOR !')
    usuarioNumero = int(input('ESCREVA UM NÚMERO DE 0 A 5 :'))
    print('processando...')
    print(f'-=-' * 20)
    c += 1
    sleep(1)
print('VOCÊ GANHOU DO COMPUTADOR')
print(f'FORAM NECESSÁRIOS {c} PALPITES PARA VENCER')