from time import sleep
class livro:
    def __init__(self, nome='', paginas=0):
        self.nome = nome
        self.paginas = paginas
        self.pagina_atual = 1

        print(f'Você acabou de abrir o livro {self.nome} que tem {self.paginas} paginas no total. Você agora está na página {self.pagina_atual}')

    def avancar_paginas(self, qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f'\nPag {self.pagina_atual} -> ', end='')
                sleep(0.5)
                cont += 1
        print(f'Você avançou {cont} páginas e agora está na página {self.pagina_atual}')
        if self.fim_do_livro():
            print(f'Você chegou ao final do livro {self.nome}.')

    def fim_do_livro(self) -> bool:
        if self.pagina_atual == self.paginas:
            return True
        else:
            return False


l1 = livro('O ÚNICO CAMINHO', 20)
l1.avancar_paginas(5)
l1.avancar_paginas(5)
l1.avancar_paginas(10)


