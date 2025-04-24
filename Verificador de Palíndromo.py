# Verificador de Palíndromo:
frase=str(input('Digite aqui a frase')).lower().strip()
for c in range (0, 1, 1):
    frase_format=frase.replace(" ", "")
    fac = frase_format[::-1]
    if fac == frase_format:
        print ('A frase "{}" é um PALÍNDROMO!!'.format(frase))
    else:
        print ('A frase "{}" não é um PALÍNDROMO!!'.format(frase))
