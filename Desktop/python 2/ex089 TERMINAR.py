ficha = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    opção = str(input('Quer continuar?: ')).strip().upper()
    if opção in 'Nn':
        print('Finalizado.')
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print()
for i, a in enumerate(ficha):
    print(f'{i}{a[0]}{a[2]}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (00 PARA INTERROMPER): '))
    if opc == 00:
        print('FINALIZADO')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc] [0]} são {ficha[opc] [1]}')
print()