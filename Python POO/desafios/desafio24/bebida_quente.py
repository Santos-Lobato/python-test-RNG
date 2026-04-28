from abc import ABC, abstractmethod

class BebidaQuente(ABC):

    def preparar(self):
        self.ferver_agua()
        self.misturar()
        self.servir()

    def ferver_agua(self):
        print('---INICIANDO PREPARO---\n1. Fervendo água a temperatura de 100ºC')

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

