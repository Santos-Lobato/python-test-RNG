
import random

def gerar_massa_teste(quantidade=1000):
    # Gera números entre 0 e 36
    numeros = [str(random.randint(0, 36)) for _ in range(quantidade)]
    # Une todos em uma string separada por espaços
    print(" ".join(numeros))

# Gera 1000 números para você copiar
gerar_massa_teste(1000)
