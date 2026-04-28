n1=float(input('Primeira nota: '))
n2=float(input('Segunda nota: '))
m = (n1+n2) / 2
if m < 5.0:
    print('Sua média foi {}'.format(m))
    print('REPROVADO')
    m = (n1 + n2) / 2
elif m > 7.0:
    print('Sua média foi {}'.format(m))
    print('APROVADO')
    m = (n1 + n2) / 2
elif m > 4.9 or m < 7.0:
    print('Sua média foi {}'.format(m))
    print('RECUPERAÇÃO')
    m = (n1 + n2) / 2


