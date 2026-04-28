pessoas = list()
infos = list()
mai = men = 0

while True:
    infos.append(str(input('Nome: ')))
    infos.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = infos[1]
    else:
        if infos[1] > mai:
            mai = infos[1]
        if infos[1] < men:
            men = infos[1]
    pessoas.append(infos[:])
    infos.clear()
    opção = str(input('Quer continuar? [S/N] '))
    if opção in 'nN':
        break

print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {mai}. Peso de ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}. Peso de ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()



