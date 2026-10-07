gastos = [60.0, 25.5, 110.0, 15.0, 80.5]

print(f"Nº gastos: {len(gastos)}") 
print(f"Total: {sum(gastos):.2f}€") 
print(f"Menor: {min(gastos):.2f}€") 
print(f"Media: {sum(gastos) / len(gastos):.2f}€") 

gastos.append(40.5) 
print(f"Tras añadir -> Total: {sum(gastos):.2f}€, Media: {sum(gastos) / 
len(gastos):.2f}€") 

grandes = [] 
for v in gastos: 
  if v > 50: 
    grandes.append(v) 
print("Superiores a 50€:", grandes)
