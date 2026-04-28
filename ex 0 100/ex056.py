somaidade = 0
mediaidade = 0

maioridadehomem = 0
nomevelho = ''

quantmulher = 0

for c in range(1, 5):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: '))
    somaidade += idade

    if c == 1 and sexo in 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome


    if sexo in 'F' and idade < 20:
        quantmulher += 1


mediaidade = somaidade / 4


print('A média da idade entre os 4 é {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomevelho))
print('A quatidade de mulheres menores de 20 anos é {}'.format(quantmulher))




