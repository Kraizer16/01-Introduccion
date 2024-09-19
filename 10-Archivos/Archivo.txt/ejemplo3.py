import io

fd = open("10-Archivos/data.txt", "r")

cad = fd.readlines()
print(cad)

fd.close()