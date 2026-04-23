import random
pr=input('Primeiro aluno: ')
seg=input('Segundo aluno: ')
ter=input('Terceiro aluno: ')
quar=input('Quarto aluno: ')
lista=[pr,seg,ter,quar]
escolhido=random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))