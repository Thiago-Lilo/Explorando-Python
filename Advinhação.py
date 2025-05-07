from random import randint
player=int(input("Advinhe qual número estou pensando, entre 1 e 10: "))
print("="*30)
pc=randint(0,10)
tentativas = 0
while player != pc:
    if player < pc:
        playerac=int(input("Maior... tente novamente:"))
        print("=" * 30)
        player=playerac
        tentativas = tentativas + 1
    if player > pc:
        playerac = int(input("Menor... tente novamente:"))
        print("=" * 30)
        player = playerac
        tentativas = tentativas + 1
print("O número pensado foi {}, você acertou!!\nNúmero de tentativas: {}".format(pc,tentativas+1))
