from dataclasses import dataclass

class ConstraintError(Exception):
    pass

@dataclass(frozen=True)
class Vehiculo:
    id: int
    nombre: str
    email: str
    

class TablaClientes: 
    def __init__(self): 
        self._filas = {} 

    def insert(self, c):
        if c.id in self._filas:
            raise ConstraintError(f"PRIMARY KEY duplicada: {c.id}")
        
        if not c.nombre:
            raise ConstraintError("NOT NULL violado: nombre")
        
        if "@" not in c.email:
            raise ConstraintError(f"CHECK violado: email {c.email!r}")
        self._filas[c.id] = c

    def count(self): 
        return len(self._filas)

tabla = TablaClientes()
datos = [
Vehiculo(1, "Seat", "ana@rmail.com"),
Vehiculo(2, "Ford", "bob@mail.com"),
Vehiculo(1, "Opel", "charlie@mail.com"),
Vehiculo(3, "", "david@mail.com"),
Vehiculo(4, "Audi", "eve@mail.com"),
]

for fila in datos:
    try:
        tabla.insert(fila)
        print(f"OK id={fila.id}")
    except ConstraintError as e:
        print(f"ERROR {e}")
print("Filas:", tabla.count())
print(Vehiculo(1, "Ana", "ana@mail.com") == datos[0])