from collections import defaultdict

lecturas = [
    (1, "Norte", 300),
    (2, "Sur", 500),
    (3, "Norte", 700),
    (4, "Este", 1000),
    (5, "Sur", 500),
    (6, "Norte", 0), 
    (7, "Oeste", 1500)
]

def group_by(filas, clave):
    grupos = defaultdict(list)
    for f in filas:
        grupos[clave(f)].append(f)
    return grupos

def resumir(filas):
    grupos = group_by(filas, lambda f: f[1])
    return sorted(
        ((zona, len(g), sum(f[2] for f in g)) for zona, g in grupos.items()),
        key=lambda t: (-t[2], t[0]),
    )

for zona, n, total in resumir(lecturas):
    print(f"{zona:<8}| COUNT={n} | SUM={total} Wh")

print(resumir([]))
