from typing import Callable, Generic, Hashable, TypeVar 
T = TypeVar("T") 

class Tabla(Generic[T]): 
    def __init__(self, pk: Callable[[T], Hashable]): 
        self._pk = pk 
        self._filas: dict = {} 
        
    def insert(self, fila: T) -> None: 
        k = self._pk(fila) 
        if k in self._filas: 
            raise KeyError(f"Codigo duplicado: {k}") 
        self._filas[k] = fila 
        
    def select(self, where=lambda f: True, order_by=None, desc=False) -> list: 
        res = [f for f in self._filas.values() if where(f)] 
        if order_by: 
            res.sort(key=order_by, reverse=desc) 
        return res 
    
tabla: Tabla[tuple] = Tabla(pk=lambda f: f[0]) 
for f in [(10, "Zoe", 80), (11, "Biel", 20), (12, "Nuria", 150), (13, "Hugo", 45)]: 
    tabla.insert(f) 
    
try: 
    tabla.insert((11, "Otro", 1))
except KeyError as e: 
    print("Error:", e) 

print("WHERE puntos < 100 ORDER BY puntos ASC") 
for f in tabla.select(lambda f: f[2] < 100, lambda f: f[2], True): 
    print(f) 
    
print("WHERE puntos < 0") 
print(tabla.select(lambda f: f[2] < 0))