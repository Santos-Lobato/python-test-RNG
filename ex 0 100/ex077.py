palavras = ("Papai", "Sabão", "Iguais", "Saguão", "Uruguaio", "Álcool", "Navio", "Saída", "Piauiense", "Casa", "Tesoura", "Mascote")

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
            