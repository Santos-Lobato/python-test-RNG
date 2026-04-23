class Gaymer:
    def __init__(self, nome='', nick=''):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_favoritos(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)

    def ficha(self):
        print(f'Jogador: <{self.nick}>'
              f'\nNome: {self.nome}\n'
              f'\nJogos favoritos:')
        for num, game in enumerate(self.favoritos):
            print(f' -> {game}')


G1 = Gaymer('Reinaldo', 'R3ID0T3RR0R')
G1.add_favoritos('Paladins')
G1.add_favoritos('Need for Speed World')
G1.add_favoritos('Midnight Club: Street Racing')
G1.add_favoritos('Jack 2')
G1.add_favoritos('GTA: Vice City')
G1.ficha()



