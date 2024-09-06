s = float(input("Ingrese la cantidad de segundos"))
h = s // 3600
m = (s % 3600) // 60
sc = s % 60
print (f"La cantidad de horas son:  {h:.0f} ")
print (f"La cantidad de minutos son: {m:.0f} ")
print (f"La cantidad de segundos son: {sc:.0f} ")
