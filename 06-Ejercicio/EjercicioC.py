n = int(input("Cantidad de palabras? \n"))
pre = input("Cual es el prefijo? \n")

cpre = 0
for i in range(n):
    pal = input("Palabra: ")

    if pal.startswith(pre):
        cpre += 1
print (cpre)



