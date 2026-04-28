peso=float(input('Qual é o seu peso? (kg) '))
alt=float(input('Qual é a sua altura? (m) '))
imc = peso / (alt ** 2)

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc <=25:
    print('Você está no peso ideal.')
elif imc <=30:
    print('Você está com sobrepeso. ')
elif imc <= 40:
    print('Você está com obesidade. ')
else:
    print('Você está com obesidade mórbida.')

