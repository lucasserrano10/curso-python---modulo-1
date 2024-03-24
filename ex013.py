number = int(input('DIGITE UM NÚMERO :'))
'''ou transformamos o numero em string'''
u = number // 1 % 10
d = number// 10 % 10
c = number//100 %10
print('analisando o número...')
print(f'unidade :{u}')
print(f'dezena :{d}')
print(f'centena :{c}')