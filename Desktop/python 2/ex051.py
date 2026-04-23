n1 = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = n1 + (10 - 1) * razão
for c in range(n1, décimo, razão):
    print('{} '.format(c), end=' -> ')
print('Números: ')

