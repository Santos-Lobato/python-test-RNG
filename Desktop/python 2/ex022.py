name=str(input('Digite seu nome: ')).strip()
print('Analisando seu nome... ')
print('Seu nome em letras maiúsculas é {}' .format(name.upper()))
print('Seu nome em letras minúsculas é {}' .format(name.lower()))
print('Seu nome tem o todo {} letras' .format(len(name)-name.count(' ')))
print('Seu primeiro nome tem {} letras' .format(name.find(' ')))



