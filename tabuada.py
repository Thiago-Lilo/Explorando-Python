from math import copysign
test = 1
while test == 1:
    num = int(input("Gostaria de ver a tabuada de qual número? (Para encerrar o programa, digite um número negativo) "))
    test = copysign(1, num)
    if test == -1:
        break
    print("="*30)
    for c in range (1, 11):
        print(f"{num}x{c}={num*c}")
    print("=" * 30)
from time import sleep
print("Finalizando...")
sleep(1)
print("Programa Finalizado")
