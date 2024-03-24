frase = str(input('digite uma frase :')).upper().strip()
print(f'a letra A aparece {frase.count('A')}')
print(f'o primeiro A apareceu na posiçao {frase.find('A')+1}')
print(f'a ultima letra A apareceu na posiçao {frase.rfind('A') + 1}')