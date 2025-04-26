#Pedra, Papel, Tesoura
from time import sleep
from random import choice
jogador=str(input('Digite sua jogada:')).lower().strip()
sleep(0.5)
print('Pedra...')
sleep(1)
print('Papel...')
sleep(1)
print('Tesoouraa...')
sleep(1)
print('=='*70)
lista = ['pedra', 'papel', 'tesoura']
pc=choice(lista)
print('O jogador escolheu {}'.format(jogador))
print('O computador escolheu {}'.format(pc))
sleep(1)
print('=='*70)
if jogador == 'pedra':
    if pc == 'tesoura':
        print('Você ganhou, pois pedra esmaga tesoura!!')
    elif pc == 'papel':
        print('Você perdeu, pois papel embrulha pedra!!')
    elif pc == 'pedra':
        print('Deu empate!!')
elif jogador == 'tesoura':
    if pc == 'papel':
        print('Você ganhou, pois tesoura corta papel!!')
    elif pc == 'pedra':
        print('Você perdeu, pois pedra esmaga tesoura!!')
    elif pc == 'tesoura':
        print('Deu empate!!')
elif jogador == 'papel':
    if pc  == 'pedra':
        print('Você ganhou, pois papel embrulha pedra!!')
    elif pc == 'tesoura':
        print('Você perdeu, pois tesoura corta papel!!')
    elif pc == 'papel':
        print('Deu empate!!')
else:
    print('Opção inválida, tente novamente.')
