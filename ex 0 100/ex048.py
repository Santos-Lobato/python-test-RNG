s=0
cont=0
for c in range(1, 500+1, 2):
    if c % 3 == 0:
        s = s + c
        cont = cont + 1
print('A soma de todos os {} múltiplos entre 1 e 500 é {}'.format(cont,s))



