# 10.
# Napiš funkci, která dostane seznam souřadnic (párů čísel menších než 10,
# která určují sloupec a řádek) a vypíše je jako mapu: mřížku 10×10,
# kde na políčka která jsou v seznamu napíše X, jinde tečku. Například:
#
# nakresli_mapu([(0, 0), (1, 0), (2, 2), (4, 3), (8, 9), (8, 9)])
# X X . . . . . . . .
# . . . . . . . . . .
# . . X . . . . . . .
# . . . . X . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . X .
# Jak na to?
#
# Udělej tabulku (seznam seznamů) se samými tečkami, něco jako:
# [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']].
# Na příslušných místech nahraď tečky X-ky.
# Tabulku vypiš pomocí dvou cyklů for zanořených do sebe.



def nakresli_mapu(souradnice):
    mapa = []
    radek = []
    for zn in range(10):
        radek.append(". ")
    for ra in range(10):
        mapa.append(list(radek))
    souradnice = list(souradnice)
    for x, y in souradnice:
        mapa[y][x] = "X"
    for radek in mapa:
        print(radek)
    return mapa


print(nakresli_mapu([(0, 0), (1, 0), (2, 2), (4, 3), (8, 9), (8, 9)]))
