class produto:
    def __init__(self, nome, valor=0):
        self.nome = nome
        self.valor = valor

    def __str__(self):
        return f'Produto: {self.nome} | Preço R$:{self.valor}'


p1 = produto('Mercedez-Benz C180', '110.000')
print(p1)

p2 = produto('Corsa Classic', '18.000')
print(p2)