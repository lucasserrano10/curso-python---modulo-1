frase = str(input('DIGITE UMA FRASE :')).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ''
for letra in range(len(junto) -1,-1,-1):
    inverso += junto[letra]
if inverso == junto:
    print(inverso)
    print(frase)
    print('TEMOS UM PALÍNDROMO')
else:
    print('NÃO TEMOS UM PALÍNDROMO')
