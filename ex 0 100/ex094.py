pessoas = list()
infos = dict()
soma = media = 0
while True:
    infos.clear()
    infos['nome'] = str(input('Nome: '))
    infos['sexo'] = str(input('Sexo[M/F]: '))
    infos['idade'] = int(input('Idade: '))
    soma+=infos['idade']
    pessoas.append(infos.copy())
    opção = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if opção not in 'Ss':
        break

print(f'Ao todo foram {len(pessoas)} pessoas cadastradas')
media = soma / len(pessoas)
print(f'A média de idade é de {media:3.2f} anos. ')
print('As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p['sexo'] == 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('====ENCERRADO====')


