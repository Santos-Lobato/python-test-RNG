num = (int(input('Digite um número: ')),
       int(input('Digite um segundo número: ')),
       int(input('Digite um terceiro número: ')),
       int(input('Digite um quarto número: ')),
       int(input('Digite o quinto número: ')))
print(f'Os valores digitados foram: {num}')
print(f'O valor "9" apareceu na {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

        