lista = [10, 20, "Juan", 30, "Sergio"]
lista.append(40)
print(lista)
lista2 = ["Maria", 20]

# Metodo append
lista.append(lista2)
print(lista)

# metodo extend
lista.extend(lista2)
print(lista)

# metodo insert
lista.insert(2, 50)
print(lista)

# metodo pop
lista.pop()
print(lista)

# metodo remove
lista.remove("Sergio")
print(lista)

############
lista = [40, 30, 5, 90, 20]

# min
print(min(lista))

# max
print(max(lista))

# len
print("Tamaño Lista: ", len(lista))

# sorted
print(sorted(lista))
# Decreciente
print(sorted(lista, reverse = True))

lista = [10, 10, 40, 30, 35, 30, 60, 10]

# count
print(lista.count(10))

# split
lista = " 1 , 2 , 3 , 4 , 5 "
print(lista.split(","))
print(lista.split(",")[3])

#del
lista = [10, 10, 40, 30, 35, 30, 60, 10]
del(lista[3]) # borra la posicion de la lista 
print(lista)

#limpiar listas
lista.clear()
print(lista)
print(type(lista))

# del lista # Elimina la variable del programa
