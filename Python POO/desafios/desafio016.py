class func:
    def __init__(self, nome='', setor='', cargo=''):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def __str__(self):
        return f'Olá, sou {self.nome} e sou {self.cargo} do setor {self.setor} na empresa Curso em Vídeo.'


f1 = func('Sérgio','T.I', 'Programador')
print(f1)