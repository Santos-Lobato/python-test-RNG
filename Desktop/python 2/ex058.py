from random import randint
computador = randint(0, 10)
num = int(input('Escolha um número entre 0 e 10: '))
while num != computador:
    num = int(input('Continue tentando: '))
print('Parabéns! o Número que foi sorteado foi {}'.format(num))
