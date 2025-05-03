r1=float(input('Digite aqui a medida da primeira reta:'))
r2=float(input('Digite aqui a medida da segunda reta:'))
r3=float(input('Digite aqui a medida da terceira reta:'))
if r1 < r2 + r3 and r3 < r2+ r1 and r2 < r3 + r1:
    if r1 == r2 and r2 == r3:
    # if r1 == r2 == r3:
       print('Estas retas irão formar um triângulo Equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Estas retas irão formar um triângulo Isóceles.')
    elif r1 != r2 or r1 != r3 or r2 != r3:
        print('Estas retas irão formar um triângulo Escaleno.')
else:
   print('Estas retas não podem formar um triângulo')