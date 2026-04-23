import math
from collections import Counter


def simulador_analise_estatistica(resultados):
    n_giros = len(resultados)
    if n_giros == 0:
        print("Nenhum dado inserido.")
        return

    # Probabilidade teórica de uma dúzia (12/37)
    p = 12 / 37

    # Média esperada (E) e Desvio Padrão Teórico (Sigma)
    media_esperada = n_giros * p
    sigma = math.sqrt(n_giros * p * (1 - p))

    # --- ANÁLISE DE DÚZIAS ---
    duzias = {
        "1ª Dúzia (1-12)": len([n for n in resultados if 1 <= n <= 12]),
        "2ª Dúzia (13-24)": len([n for n in resultados if 13 <= n <= 24]),
        "3ª Dúzia (25-36)": len([n for n in resultados if 25 <= n <= 36]),
        "Zero (Casa)": len([n for n in resultados if n == 0])
    }

    print(f"\n{'=' * 40}")
    print(f"--- RELATÓRIO DE ANÁLISE: {n_giros} RODADAS ---")
    print(f"{'=' * 40}")
    print(f"Média Esperada por Dúzia: {media_esperada:.2f}")
    print(f"Desvio Padrão Teórico (1σ): {sigma:.2f}\n")

    for nome, qtd in duzias.items():
        if "Zero" in nome:
            porcentagem_zero = (qtd / n_giros) * 100
            print(f"{nome}: {qtd} ocorrências ({porcentagem_zero:.1f}%)")
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
        print(f"  - Z-Score: {z_score:+.2f}σ")
        print(f"  - Status: {classificacao}\n")

    # --- ANÁLISE DE NÚMEROS QUENTES E FRIOS ---
    # Contamos a frequência de todos os números possíveis (0 a 36)
    contagem = Counter(resultados)
    frequencia_total = {i: contagem.get(i, 0) for i in range(37)}

    # Ordenar números por frequência
    # Quentes: do maior para o menor | Frios: do menor para o maior
    ordenados = sorted(frequencia_total.items(), key=lambda x: x[1], reverse=True)

    quentes = ordenados[:5]
    frios = ordenados[-5:]

    print("-" * 40)
    print("🔥 TOP 5 NÚMEROS QUENTES (Mais sorteados)")
    for num, freq in quentes:
        perc = (freq / n_giros) * 100
        print(f"  Número {num:02d}: {freq}x ({perc:.1f}%)")

    print("\n❄️ TOP 5 NÚMEROS FRIOS (Menos sorteados)")
    # Re-ordenar os frios para mostrar os menores primeiro
    for num, freq in sorted(frios, key=lambda x: x[1]):
        perc = (freq / n_giros) * 100
        print(f"  Número {num:02d}: {freq}x ({perc:.1f}%)")
    print("-" * 40)


# --- ENTRADA DE DADOS ---
print("Simulador de Roleta Profissional")
entrada = input("Cole os números separados por espaço: ")

try:
    resultados = list(map(int, entrada.split()))
    simulador_analise_estatistica(resultados)
except ValueError:
    print("Erro: Certifique-se de inserir apenas números separados por espaços.")