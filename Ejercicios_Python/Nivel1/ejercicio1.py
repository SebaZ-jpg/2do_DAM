# cada variable guarda tengo, número, etc, los decimales usan PUNTO  
producto = "raton"
precio = 12.5
unidades = 4
tipo_iva = 10

base = precio * unidades
cuota_iva = base * tipo_iva / 100
total = base + cuota_iva

# usamos el print para mostrar en pantalla lo que hay entre parentesis
print(f"{producto} x {unidades}")    

# : .2f significa que queremos mostrar 2 decimales y f es de float
print(f"Base: {base:.2f}€") 

# el % son texto normal que se escribe tal cual; solo lo que está entre llaves cambia. {tipo_iva} pasa a 10 y {cuota_iva:.2f} pasa a 5.00.
# Resultado: IVA (10%): 5.00€
print(f"IVA ({tipo_iva}%): {cuota_iva:.2f}€")

# muestra el total con 2 decimales y el símbolo del euro
print(f"Total: {total:.2f}€") 

# type(...) le pregunta a Python “¿de qué tipo es este dato?”. 
# Aquí se pregunta por tres variables a la vez, y print las escribe en una sola línea separadas por un espacio
print(type(producto), type(precio), type(unidades))