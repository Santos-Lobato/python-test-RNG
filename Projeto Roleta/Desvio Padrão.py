import math

def simulador_analise_estatistica(resultados):

    n_giros = len(resultados)

    # Probabilidade teórica de uma dúzia (12/37)
    p = 12 / 37

    # Média esperada (E) e Desvio Padrão Teórico (Sigma)
    media_esperada = n_giros * p
    sigma = math.sqrt(n_giros * p * (1 - p))

    # Contabilidade dos grupos
    duzias = {
        "1ª Dúzia (1-12)": len([n for n in resultados if 1 <= n <= 12]),
        "2ª Dúzia (13-24)": len([n for n in resultados if 13 <= n <= 24]),
        "3ª Dúzia (25-36)": len([n for n in resultados if 25 <= n <= 36]),
        "Zero (Casa)": len([n for n in resultados if n == 0])
    }

    print(f"--- RELATÓRIO DE ANÁLISE: {n_giros} RODADAS ---")
    print(f"Média Esperada por Dúzia: {media_esperada:.2f}")
    print(f"Desvio Padrão Teórico (1σ): {sigma:.2f}\n")

    for nome, qtd in duzias.items():

        if "Zero" in nome:
            print(f"{nome}: {qtd} ocorrências")
            continue

        z_score = (qtd - media_esperada) / sigma
        porcentagem = (qtd / n_giros) * 100

        if abs(z_score) <= 1:
            classificacao = "Dentro da normalidade"
        elif 1 < abs(z_score) <= 2:
            classificacao = "Desvio moderado"
        elif 2 < abs(z_score) <= 3:
            classificacao = "DESVIO SIGNIFICATIVO"
        else:
            classificacao = "ANOMALIA EXTREMA"

        print(f"{nome}:")
        print(f"  - Sorteados: {qtd} ({porcentagem:.1f}%)")
        print(f"  - Distância da Média: {z_score:+.2f} sigmas")
        print(f"  - Status: {classificacao}\n")


# 🔹 COLE SEUS NÚMEROS AQUI
entrada = input("Cole os números separados por espaço: ")

# Converte para lista de inteiros
resultados = list(map(int, entrada.split()))

# Executa análise
simulador_analise_estatistica(resultados)