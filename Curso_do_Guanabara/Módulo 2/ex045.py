from random import randint
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0,2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Opção: '))
print('Jô')
sleep(1)
print('Ken')
sleep(1)
print('Po!!!!')
print('-='*30)
opcomputador = itens[computador]
print(f'Computador jogou: {opcomputador}')
print(f'Jogador jogou: {itens[jogador]}')
print('-='*30)
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Vence')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('Jogada inválida')
elif computador == 1:
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador Vence')
    else:
        print('Jogada inválida')
elif computador == 2:
    if jogador == 0:
        print('Jogador Vence')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida')
else:
    print('Jogada inválida')
