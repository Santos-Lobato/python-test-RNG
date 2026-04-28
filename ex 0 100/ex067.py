num = 0
num2 = 0
while True:
    num = int(input('Quer ver a tabuada de qual número?: '))
    if num < 0:
        break
    for c in range(1, 11):
        print('{} x {} = {} '.format(num, c, num * c))
print('PETIÇÃO A TABUADA ENCERRADA.')

