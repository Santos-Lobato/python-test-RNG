class Pessoa:
    def __init__(self, nome='', idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'\nO Aluno {self.nome} acabou de fazer a matrícula.')

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'O professor {self.nome} começou a dar aula.')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f'O funcionário {self.nome} bateu o ponto.')


A1 = Aluno('Jamal', 23, 'Ciencia da Computação', '4003\n')
A1.fazer_aniversario()
A1.fazer_matricula()
print(A1.nome)
print(A1.idade)
print(A1.curso)
print(A1.turma)

A2 = Professor('Fernando', 42, 'Economia', 'PhD\n')
A2.fazer_aniversario()
A2.dar_aula()
print(A2.nome)
print(A2.idade)
print(A2.especialidade)
print(A2.nivel)

A3 = Funcionario('Rogério', 35, 'Tech Lead', 'T.I\n')
A3.fazer_aniversario()
A3.bater_ponto()
print(A3.nome)
print(A3.idade)
print(A3.cargo)
print(A3.setor)
