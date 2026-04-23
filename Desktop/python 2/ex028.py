from random import randint
computador = randint(0, 5)

print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')

jogador=int(input('Em que número eu pensei? '))
if jogador == computador:
    print('PARBÉNS! Você conseguiu me vencer!')
else:
    print('Ganhei! O número é {} e não {}'.format(computador, jogador))


