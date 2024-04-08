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
    jUser = str(input('PAR OU IMPAR ?')).strip().lower()
    while jUser not in ('impar' or 'par'):
        jUser = str(input('PAR OU IMPAR ?')).strip().lower()
    nComputador = choice(numeros)
    if jUser == "par":
        jComputador = "impar"
    elif jUser == "impar":
        jComputador = "par"
    print(f'ANALISANDO...')
    sleep(2)
    print(f'-' * 25)
    print(f'USUÁRIO, NÚMERO :{nUser}, JOGADA: {jUser}')
    print(f'COMPUTADOR, NÚMERO:{nComputador}, JOGADA: {jComputador}')
    print(f'-' * 25)
    if (nComputador + nUser) % 2 == 0:
        if jUser == "par":
            print('VOCÊ GANHOU !')
            contadorVitoriasUsuario += 1
        else:
            print(f'-' * 25)
            print(f'COMPUTADOR GANHOU !, VOCÊ VENCEU {contadorVitoriasUsuario} VEZES')
            break


