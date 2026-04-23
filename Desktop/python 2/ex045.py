from random import randint
itens = ('Pedra', 'papel', 'Tesoura')
computador = randint(0,2)

print('''Suas opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA : ''')


jogador=int(input('Qual é a sua jogada? '))


print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))


if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada INVÁLIDA')

elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada INVÁLIDA')

elif computador == 2: #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada INVÁLIDA')




