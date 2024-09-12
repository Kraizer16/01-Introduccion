from unittest import result


def posElemMayList(lst):
    mayor = lst[0]
    pos = 0
    for i in range(len(lst)):
        if lst[i] > mayor:
            mayor = lst[i]
            pos = i
    return [pos, mayor]


def posMayList(lst):
    mayor = lst[0]
    pos = 0
    for i in range(len(lst)):
        if lst[i] > mayor:
            mayor = lst[i]
            pos = i
    return pos



def menorLista(lst):
    menor = lst[0]
    for e in lst:
        if e > menor:
            menor = e
    return menor



def mayorLista(lst):
    mayor = lst[0]
    for e in lst:
        if e > mayor:
            mayor = e
    return mayor
        

def sumaLista(lst):
    suma = 0
    for e in lst:
        suma += e
    return suma



def imprimeLista(lst):
    for e in lst:
        print(e, end = " | ")


lista_numeros = [10, 15, 20, 30, 40]

print(type(lista_numeros))

print(lista_numeros)

print(lista_numeros[3])

print(lista_numeros[-1])

# Recorre una lista
# 1. por sus posiciones

for i in range(len(lista_numeros)):
    print(lista_numeros[i], end=", ")
print("")

for i in range(-1, -len(lista_numeros)-1, -1):
    print(lista_numeros[i], end = "* ")
print(" ")

for i in range(len(lista_numeros)-1, -1,-1):
    print(lista_numeros[i], end = "-")
print(" ")

#2. por sus elementos

for e in lista_numeros:
    print(e, end ="; ")

print(" ")

# LLamado a una funcion. Se le pasa la lista
imprimeLista(lista_numeros)
print("")


#funcion que devuelva la suma de los elementos de la lista
print("La suma de los elementos de la lista es: ", sumaLista(lista_numeros))

# Imprimir el mayor elemento de la lista
print("El mayor elemento es: ", mayorLista(lista_numeros))

# Imprimir el menor elemento de la lista
print("El menor elemento de la lista es: ", menorLista(lista_numeros))

# Imprimir la posicion del elemento mayor de la lista

print("El elemento mayor se encuentra en la posicion: ", posMayList(lista_numeros) + 1)

# Imprimir la posicion y el vlaor del elemento mayor de la lista

print("El elemento mayor se encuentra en la posicion: ", posElemMayList(lista_numeros)[1], posElemMayList(lista_numeros)[0] + 1,)

# Con variable mas eficiente
resulta = posElemMayList(lista_numeros)
print("El elemento mayor se encuentra en la posicion: ", resulta[1], ("|"), result[0] + 1 )

# Modificar una lista
# lista_numeros = [10, 15, 20, 30, 40]

lista_numeros[-1] = 35 #lista_numeros[4] = 35

# operadores de las listas
lista_numero2 = [1, 2]

# operador de concatenacion (+)
lstrslt = lista_numero2 + lista_numeros
print(lstrslt)

# operador de repeticion (*)
lstrslt = lista_numero2 * 3
print(lstrslt)

# operador 