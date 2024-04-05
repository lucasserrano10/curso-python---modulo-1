from random import choice
from time import sleep
numeros = [1,2,3,4,5,6,7,8,9,10]
jComputador = ''
contadorVitoriasUsuario = 0

print(f'-'*25)
print(f'VAMOS JOGAR PAR OU IMPAR')
print(f'-'*25)

while True:
    nUser = int(input('DIGA UM NÚMERO :'))
    jUser = str(input('PAR OU IMPAR ?')).strip().upper()
    nComputador = choice(numeros)
    if jUser == "PAR":
        jComputador = "IMPAR"
    elif jUser == "IMPAR":
        jComputador = "PAR"
    print(f'ANALISANDO...')
    sleep(3)
    print(f'-' * 25)
    print(f'USUÁRIO, NÚMERO :{nUser}, JOGADA: {jUser}')
    print(f'-' * 25)
    print(f'COMPUTADOR, NÚMERO:{nComputador}, JOGADA: {jComputador}')
    print(f'-' * 25)
    if (nComputador + nUser) % 2 == 0:
        if jUser == "PAR":
            print('USUÁRIO GANHOU !')
            contadorVitoriasUsuario += 1
        else:
            print(f'COMPUTADOR GANHOU !, VOCÊ VENCEU {contadorVitoriasUsuario} VEZES')
            break


