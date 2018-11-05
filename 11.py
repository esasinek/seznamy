# 11.
# Napiš funkci pohyb, která dostane seznam souřadnic a světovou stranu ("s", "j", "v" nebo "z")
# a přidá k seznamu poslední bod „posunutý“ v daném směru. Např.:

# souradnice = [(0, 0)]
# pohyb(souradnice, 'v')
# print(souradnice)         # → [(0, 0), (1, 0)]
# pohyb(souradnice, 'v')
# print(souradnice)         # → [(0, 0), (1, 0), (2, 0)]
# pohyb(souradnice, 'j')
# print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1)]
# pohyb(souradnice, 's')
# print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1), (2, 0)]
# Funkce by neměla nic vracet. Jen mění už existující seznam.

souradnice = [(0, 0)]

def pohyb(souradnice, strana):
    x = souradnice[-1][0]
    y = souradnice[-1][1]
    if strana == "v":
        x += 1
        nova = x, y
        souradnice.append(nova)
    elif strana == "j":
        y += 1
        nova = x, y
        souradnice.append(nova)
    elif strana == "s":
        y -= 1
        nova = x, y
        souradnice.append(nova)
    elif strana == "z":
        x -= 1
        nova = x, y
        souradnice.append(nova)


pohyb(souradnice, "v")
print(souradnice)
pohyb(souradnice, "j")
print(souradnice)
pohyb(souradnice, "s")
print(souradnice)
pohyb(souradnice, "z")
print(souradnice)
