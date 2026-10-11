empleados = [
    {"id": 1, "nombre": "Ana", "dep_id": 10}, 
    {"id": 2, "nombre": "Luis", "dep_id": 20}, 
    {"id": 3, "nombre": "Eva", "dep_id": None}, 
    {"id": 4, "nombre": "Pau", "dep_id": 99}, ]

departamentos = [ 
    {"id": 10, "nombre": "Ventas"},
    {"id": 20, "nombre": "IT"},
    {"id": 30, "nombre": "RRHH"}, 
    
]

def inner_join(izq, der, col_izq, col_der="id"): 
    indice = {d[col_der]: d for d in der} 
    return [(i, indice[i[col_izq]]) for i in izq if i[col_izq] in indice] 

def left_join(izq, der, col_izq, col_der="id"): 
    indice = {d[col_der]: d for d in der} 
    return [(i, indice.get(i[col_izq])) for i in izq] 

print("INNER JOIN") 
for e, d in inner_join(empleados, departamentos, "dep_id"): 
    print(f"{e['nombre']} -> {d['nombre']}") 
print("LEFT JOIN") 
for e, d in left_join(empleados, departamentos, "dep_id"): 
    print(f"{e['nombre']} -> {d['nombre'] if d else 'NULL'}") 
    
print(inner_join([], departamentos, "dep_id"))