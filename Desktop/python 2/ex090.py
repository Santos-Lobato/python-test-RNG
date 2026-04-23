aluno = {'nome': str(input('Nome: '))}
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
aluno['situação'] = 'aprovado' if aluno ['media'] >= 7 else 'reprovado'

for key, value in aluno.items():
    print(f'{key}:', value)
