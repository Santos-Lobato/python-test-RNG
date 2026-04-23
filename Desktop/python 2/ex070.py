somaproduto = preçomaior = cont = menor = 0
while True:
    produto = str(input('Nome do Produto: '))
    preço = int(input('Preço R$: '))
    cont += 1
    somaproduto += preço
    if preço >= 1000:
        preçomaior += 1
    if cont == 1:
        menor = preço
    else:
        if preço < menor:
            menor = preço
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi {somaproduto}')
print(f'Temos {preçomaior} produtos custando mais de R$:1000.')
print(f'O produto mais barato custa R$:{menor:.2f}')
