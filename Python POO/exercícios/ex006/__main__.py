from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

def main():

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

if __name__ == "__main__":
    main()

