from time import sleep
def maior(*num ):
    cont = maior = 0
    print('\nAnalisando os números...')
    for valor in num:
        print(f'{valor} ',end='', flush=True)
        sleep(0.4)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foraam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}. ')

    
#programa principal
maior(2, 3, 4, 67, 7, 9)
maior(8, 9, 0)
maior(10, 13)
maior(8)
