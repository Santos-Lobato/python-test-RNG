from datetime import date
atual = date.today().year
ano=int(input('Ano de nascimento: '))
idade = atual - ano
print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Classificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL ')
elif idade > 14 and idade <= 19:
    print('Classificação: JUNIOR')
elif idade > 19 and idade <=25:
    print('CLassificação: SÊNIOR')
elif idade > 25:
    print('Classificação: MASTER')
    

