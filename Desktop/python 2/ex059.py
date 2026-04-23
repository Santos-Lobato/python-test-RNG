from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor '))

opção = 0
while opção != 5:
    print(''' 
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    
    opção = int(input('Qual é a sua opção?: '))
    if opção == 1:
                print('{} + {} = {}'.format(n1, n2, n1+n2))
    elif opção == 2:
                print('{} x {} = {}'.format(n1, n2, n1*n2))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else: maior = n2
        print('entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente!')
        n1= int(input('Primeiro valor: '))
        n2= int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente.')
    sleep(2)
print('Fim do programa!')



