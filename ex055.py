n1 = int(input('DIGITE UM NÚMERO :'))
n2 = int(input('DIGITE OUTRO NÚMERO :'))
c = 0
while c != 1:
    escolha: int = int(input(f'QUAL OPERAÇÃO DESEJA FAZER ? \n [1]soma\n [2]subtração\n [3]multiplicação\n [4]divisão\n [5]sair do programa :'))
    if escolha == 5:
        c = 1
        print(f'-=-' * 20)
    elif escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4 and escolha != 5:
        print('OPÇÃO INVÁLIDA')
        print(f'-=-' * 20)
    elif escolha == 4:
        print(f'a divisão é {n1/n2}')
        print(f'-=-' * 20)
    elif escolha == 3:
        print(f'a multiplicação é {n1 * n2}')
        print(f'-=-' * 20)
    elif escolha == 2:
        print(f'a subtração é {n1 - n2}')
        print(f'-=-' * 20)
    else:
        print(f'a soma é {n1 + n2}')
        print(f'-=-' * 20)



