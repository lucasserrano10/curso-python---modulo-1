nome = str(input('NOME COMPLETO :')).strip()
n = nome.split()
print(f'seu primeiro nome é {n[0]}')
print(f'seu ultimo nome é {n[len(n)-1]}')