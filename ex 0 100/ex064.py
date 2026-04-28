num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    cont = cont + 1
    soma += num
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))
print('FIM')
