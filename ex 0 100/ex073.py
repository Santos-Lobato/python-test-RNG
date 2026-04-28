times = (
    "Palmeiras",
    "São Paulo",
    "Bahia",
    "Fluminense",
    "Coritiba",
    "Flamengo",
    "Athletico-PR",
    "Grêmio",
    "Corinthians",
    "Vasco da Gama",
    "Atlético-MG",
    "Bragantino",
    "EC Vitória",
    "Chapecoense",
    "Mirassol",
    "Santos",
    "Internacional",
    "Botafogo",
    "Remo",
    "Cruzeiro"
)
print('+=' * 15)
print(f'Listas de times dos brasileirão: {times}')
print('+=' * 15)
print(f'Os 5 primeiros são {times[:5]}')
print('+=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('+=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('+=' * 15)
print(f'O Flamengo está na {times.index("Flamengo")+1}ª posição')
print('+=' * 15)