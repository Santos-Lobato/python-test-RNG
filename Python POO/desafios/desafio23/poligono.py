from math import pi
from abc import ABC, abstractmethod


class Poligono (ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * 2

    def calcular_perimetro(self):
        return self.lado * 4


class Circulo(Poligono):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return pi * (self.raio ** 2)

    def calcular_perimetro(self):
        return 2 * (pi * self.raio)


