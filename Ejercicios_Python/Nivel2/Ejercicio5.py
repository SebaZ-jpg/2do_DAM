from itertools import islice 

def leer_filas(filas): 
    for f in filas: 
        print(f"  [cargando {f['id']}]") 
        yield f 
        
def limit_offset(it, limit, offset=0): 
    return list(islice(it, offset, offset + limit)) 

filas = [{"id": i, "titulo": f"Tema{i}"} for i in range(1, 7)] 

print("LIMIT 3 OFFSET 2") 
pag = limit_offset(leer_filas(filas), 3, 2) 

print([f["titulo"] for f in pag]) 
print("LIMIT 2 OFFSET 20") 
print(limit_offset(leer_filas(filas), 2, 20)) 

print("Cursor perezoso") 
c = leer_filas(filas) 
print(next(c)["titulo"]) 
print(next(c)["titulo"])