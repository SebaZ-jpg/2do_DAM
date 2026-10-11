from collections import defaultdict     
        
pedidos = [ 
    (1, "Madrid", 1500), 
    (2, "Sevilla", 800), 
    (3, "Madrid", 2500), 
    (4, "Bilbao", 1200), 
    (5, "Sevilla", 400), 
    (6, "Madrid", 100), 
    
]

def group_by(filas, clave): 
    grupos = defaultdict(list) 
    for f in filas: 
        grupos[clave(f)].append(f) 
    return grupos 

def resumen(filas): 
    grupos = group_by(filas, lambda f: f[1]) 
    return sorted( 
        ((ciudad, len(g), sum(f[2] for f in g)) for ciudad, g in grupos.items()), 
        key=lambda t: (-t[2], t[0]), 
    ) 

for ciudad, n, total in resumen(pedidos): 
    print(f"{ciudad:<8}| COUNT={n} | SUM={total} cent") 

print(resumen([]))