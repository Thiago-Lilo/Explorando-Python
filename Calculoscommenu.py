n1=int(input("Digite aqui o primeiro número"))
n2=int(input("Digite aqui o segundo número"))
print("="*20)
operador = 0
while operador != 5:
    operador = int(input("Digite a operação desejada:\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair do programa\n"))
    if operador == 1:
        print("=" * 20)
        print("A soma dos números {} e {} é {}".format(n1, n2, n1+n2))
        print("=" * 20)
    elif operador == 2:
        print("=" * 20)
        print("A multiplicação dos números {} e {} é {}".format(n1, n2, n1 * n2))
        print("=" * 20)
    elif operador == 3:
        if n1 > n2:
            print("=" * 20)
            print("O maior número é {}".format(n1))
            print("=" * 20)
        elif n2 > n1:
            print("=" * 20)
            print("O maior número é {}".format(n2))
            print("=" * 20)
    elif operador == 4:
        print("=" * 20)
        n1 = int(input("Digite aqui o primeiro novo número"))
        n2 = int(input("Digite aqui o segundo novo número"))
        print("=" * 20)
    elif operador == 5:
        print("=" * 20)
        print("FIM")
        break
