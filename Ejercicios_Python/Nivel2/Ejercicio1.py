from dataclasses import dataclass

class RestriccionError(Exception):
    pass

@dataclass(frozen=True)
class Vehiculo:
    matricula: str
    marca: str
    km: str

class TablaVehiculos:
    def __dict__(self):
        self._filas = {}

    def insert(self, c):
        if c.id in self._filas:
            raise RestriccionError(f"PRIMARY KEY duplicada: {matricula}")
        
        if not c.nombre:
            raise RestriccionError("NOT NULL violado: marca")
        
        if "@" not in c.email:
            raise RestriccionError(f"CHECK violado: km {c.valor!r}")
        self._filas[c.id] = c

    def count(self): 
        return len(self._filas)

tabla = TablaClientes()
datos = [
Vehiculo("1111AAA", "Seat", 520000),
Vehiculo("2222BBB", "Ford", 0),
Vehiculo("1111AAA", "Opel", 10),
Vehiculo("3333CCC", "", 500),
Vehiculo("4444DDD", "Audi", -5),
]

for fila in datos:
    try:
        tabla.insert(fila)
        print(f"OK id={fila.id}")
    except ConstraintError as e:
        print(f"ERROR {e}")
print("Filas:", tabla.count())
print(Vehiculo(1, "Ana", "ana@mail.com") == datos[0])