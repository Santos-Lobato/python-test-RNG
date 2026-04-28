v=float(input('Qual é o valor da casa? '))
s=float(input('Qual é o salário do comprador? '))
anosf=int(input('Serão quantos anos de financiamento? '))
paremp = v/(anosf * 12)
print('Para pagar uma casa de R$:{:.2f} em {} anos, a prestação será de R$:{:.2f}'.format(v, anosf, paremp))

min=(s*30) / 100

if paremp <= min:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO!')







