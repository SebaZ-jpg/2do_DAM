libros = [
    {"id": 1, "titulo": "El Quijote", "autor_id": 1},
    {"id": 2, "titulo": "Ficciones", "autor_id": 2},
    {"id": 3, "titulo": "Anonimo", "autor_id": None},
    {"id": 4, "titulo": "Emma", "autor_id": 77},
]

autores = [
    {"id": 1, "nombre": "Cervantes"},
    {"id": 2, "nombre": "Borges"},
    {"id": 3, "nombre": "Austen"},
]

def inner_join(izq, der, col_izq, col_der="id"):
    indice = {d[col_der]: d for d in der}
    return [(i, indice[i[col_izq]]) for i in izq if i[col_izq] in indice]

def left_join(izq, der, col_izq, col_der="id"):
    indice = {d[col_der]: d for d in der}
    return [(i, indice.get(i[col_izq])) for i in izq]

print("INNER JOIN")
for l, a in inner_join(libros, autores, "autor_id"):
    print(f"{l['titulo']} -> {a['nombre']}")
print("LEFT JOIN")
for l, a in left_join(libros, autores, "autor_id"):
    print(f"{l['titulo']} -> {a['nombre'] if a else 'NULL'}")

print(inner_join([], autores, "autor_id"))