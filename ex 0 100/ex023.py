NMR=int(input('Insira um número: '))

u = NMR // 1 % 10
d = NMR // 10 % 10
c = NMR // 100 % 10
m = NMR // 1000 % 10
print('Analisando o número...'.format(NMR))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('milhar: {}'.format(m))


