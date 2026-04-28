#Declaração de Classe

class rooligan:
    def __init__(self, nome):
        # Atributo de Instância
        self.nome = nome
        self.idade = 0

    # Método de Instância
    def aniversário(self):
        self.idade += 1

    def mensagem(self):
        return f'{self.nome} é Rooligan e tem {self.idade} anos de idade'

#Declaração de Objetos
r1 = rooligan('')
r1.nome = "Robert"
r1.idade = 21
r1.aniversário()
print(r1.mensagem())

r2 = rooligan('')
r2.nome = "Florença"
r2.idade = 22
r2.aniversário()
print(r2.mensagem())

