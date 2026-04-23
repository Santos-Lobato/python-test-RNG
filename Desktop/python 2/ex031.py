distancia=float(input('Qual é distância de sua viagem? '))
print('Você está prestes a começar um vigem de {} km.'.format(distancia))
preço=distancia * 0.50 if distancia<=200 else distancia * 0.45
print('O preço de sua passagem será de R${:.2f}'.format(preço))

