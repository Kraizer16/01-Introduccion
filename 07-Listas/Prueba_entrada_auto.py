# Algoritmo que duplique los n datos ingresados

def duplicador(lst):
    lrta = []
    for e in lst:
        lrta.append(e * 2)
    
    return lrta

n = int(input("Ingrese la cantidad de datos: "))
lstnum = []
for i in range (n):
    lstnum.append(int(input(f"Ingrese el dato #{i+1}: ")))

print(", ".join(duplicador(lstnum)))