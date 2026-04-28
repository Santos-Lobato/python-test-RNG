sexo = str(input('Sexo: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. por favor, informe seu SEXO: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
