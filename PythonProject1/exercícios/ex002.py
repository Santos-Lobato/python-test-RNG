#Declaração de Classe

class rooligan:
    def __init__(self, nome='', idade = 0):
        # Atributo de Instância
        self.nome = nome
        self.idade = idade

    # Método de Instância
    def aniversário(self):
        self.idade += 1

    def __str__(self): #Dunder Attribute
        return f'{self.nome} é Rooligan e tem {self.idade} anos de idade'

    def __getstate__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade}'

#Declaração de Objetos
r1 = rooligan('Robert', 17)
r1.aniversário()
print(r1)
print(r1.__dict__) #attribute
print(r1.__getstate__()) #method
print(r1.__class__)
print(r1.__doc__)






