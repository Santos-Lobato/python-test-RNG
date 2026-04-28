from poligono import *

def main():

    p1 = Circulo(5)
    print(f'Perímetro = {p1.calcular_perimetro():.1f}')
    print(f'Área = {p1.calcular_area():.1f}')


if __name__ == '__main__':
    main()


