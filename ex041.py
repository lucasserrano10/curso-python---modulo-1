import random
from time import sleep
jogadas = ['pedra', 'papel', 'tesoura']

print('BEM VINDO AO JOKNEPÔ GAME !')
print(f'-=-=' * 20)
print('TEMOS TRÊS TIPOS DE JOGADAS !')
print(f'-=-=' * 20)

print('pedra')
print('papel')
print('tesoura')
print(f'-=-=' * 20)

usuárioJogada = int(input('ESCOLHA UMA JOGADA, 1- PEDRA, 2- TESOURA, 3- PAPEL: '))
computadorPensamento = random.choice(jogadas)
print(f'-=-=' * 20)
print('ESPERANDO RESPOSTA DO ADVERSÁRIO...')
sleep(3)
if usuárioJogada == 1 and computadorPensamento == 'tesoura':
    print('VOCÊ GANHOU DO COMPUTADOR')
    print(f'-=-=' * 20)
    print(f'pensamento do computador foi: {computadorPensamento}')
elif usuárioJogada == 2 and computadorPensamento == 'pedra':
    print('COMPUTADOR GANHOU !')
    print(f'-=-=' * 20)
    print(f'pensamento do computador foi: {computadorPensamento}')
elif usuárioJogada == 2 and computadorPensamento == 'papel':
    print('VOCÊ GANHOU DO COMPUTADOR')
    print(f'-=-=' * 20)
    print(f'pensamento do computador foi: {computadorPensamento}')
elif usuárioJogada == 3 and computadorPensamento == 'tesoura':
    print('COMPUTADOR GANHOU !')
    print(f'-=-=' * 20)
    print(f'pensamento do computador foi: {computadorPensamento}')
elif usuárioJogada == 3 and computadorPensamento == 'pedra':
    print('VOCÊ GANHOU DO COMPUTADOR')
    print(f'-=-=' * 20)
    print(f'pensamento do computador foi: {computadorPensamento}')
elif usuárioJogada == 1 and  computadorPensamento == 'papel':
    print('COMPUTADOR GANHOU !')
    print(f'-=-=' * 20)
    print(f'pensamento do computador foi: {computadorPensamento}')
else:
    print('ESCOLHA INVÁLIDA')