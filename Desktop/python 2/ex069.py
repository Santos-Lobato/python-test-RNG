tot18 = SexoMm = menorde20 = 0

while True:
    print('CADASTRE UMA PESSOA!')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        SexoMm += 1
    if sexo == 'F' and idade < 20:
        menorde20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {SexoMm} homens cadastrados.')
print(f'São {menorde20} mulheres com menos de 20 anos.')

print('Acabou!')

