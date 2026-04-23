from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Ano de nascimento'] = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - dados['Ano de nascimento']
dados['CTPS'] = int(input('Carteira de trabalho (0 = SEM REGISTRO): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário R$: '))
    dados['Aposentadoria'] = (dados['Contratação'] + 35) - dados['Ano de nascimento']

print(dados)
for k, v in dados.items():
    print(f'{k}: {v}')

