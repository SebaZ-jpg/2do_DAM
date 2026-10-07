factura = 240
cuota = factura / 4

for n in range(1, 5):
    pagado = cuota * n
    pendiente = factura - pagado
    print(f"Cuota {n}: pagado {pagado:.2f}€ | pendiente {pendiente:.2f}€")
  
caja = 100
gastos_pagados = 0

while caja >= 30:
    caja -= 30
    gastos_pagados += 1

print(f"Gastos pagados: {gastos_pagados}, caja restante: {caja}€")
