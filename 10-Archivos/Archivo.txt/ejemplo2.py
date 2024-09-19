import io

fd = open("10-Archivos/data.txt", "r")

cad = fd.readline().strip()
print(cad)

cad = fd.readline().strip()
print(cad)

fd.close()