

# Programa principal
d_categoria = {1:25_000, 2:30_000, 3:40_000, 4:45_000
               , 5:60_000}
n = int(input("Cantidad de docentes: "))

docentes = {}
suma = 0
for i in range(n):
    print(f"\nDocente {i+1}")
    cedula = input("Cédula? ")
    dDatos = {}
    dDatos["Nombre"] = input("Nombre? ")
    dDatos["Categoria"] = int(input("Categoria (1 al 5)"))
    dDatos["Horas_lab"] = int(input("Horas Laboradas? "))
    dDatos["Honorarios"] = d_categoria[dDatos["Categoria"]]* dDatos["Horas_lab"]
    docentes[cedula] = dDatos
    suma += dDatos["Honorarios"]
# Informe
print("")
print("** INFORME **".center(40))
print("")

for k in docentes.keys():
    print("Nombre:", docentes[k]['Nombre'].title())
    print(f"Honorarios: ${docentes[k]['Honorarios']:,}")
print("")
print("-" * 30, "\n")    
print(f"Valor total de los honorarios ${suma:,}")
print("-" * 30, "\n")    