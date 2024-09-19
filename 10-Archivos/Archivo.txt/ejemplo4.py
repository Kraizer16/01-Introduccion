import io

fd = open("10-Archivos/data.txt", "r")

# RECORRIDO DE ARCHIVOS 
for linea in fd:

    print(linea.strip().title())

fd.seek(0)

for car in fd.read():
    print(car, end=",")

fd.close()