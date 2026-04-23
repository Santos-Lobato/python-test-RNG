from random import shuffle
pr=input('insira o nome do primeiro aluno: ')
seg=input('insira o nome do segundo aluno: ')
ter=input('insira o nome do terceiro aluno: ')
qua=input('insira o nome do quarto aluno: ')
lista=[pr,seg,ter,qua]
shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))

