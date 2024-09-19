import json
import pprint

def guardar(lib):
    with open("10-Archivos/libreria.json", "w") as fd:
        json.dump(lib, fd)
    
    if not fd.closed:
        fd.close()




def leerPrecio():
    while True:
        try:
            precio = int(input("Precio del libro: "))
            if precio < 500:
                print(">>> Error. Precio incorrecto")
                continue
            return precio
        except ValueError:
            print(">>>> Error. Precio inválido")

def leerAutor():
     while True:
        try:
            autor = input("Autor del libro? ")
            if len(autor.strip()) == 0:
                print(">>>ERROR. El Autor ingresado es inválido")
                continue
            return autor
        except Exception as e:
            print("Error al ingresar el Autor.\n" + e)

def leerTitulo():
     while True:
        try:
            tit = input("Título del libro? ")
            if len(tit.strip()) == 0:
                print(">>>ERROR. El Título ingresado es inválido")
                continue
            return tit
        except Exception as e:
            print("Error al ingresar el título.\n" + e)

def leerCodigo():
    while True:
        try:
            cod = input("Código del libro? ")
            if len(cod.strip()) == 0:
                print(">>> El Código inválido")
                continue
            return cod
        except Exception as e:
            print("Error al ingresar el código.\n" + e)



def Insertar(lib):
    print("\n\n**1. INSERTAR ***")

    cod = leerCodigo()
    if cod not in lib:
        titulo = leerTitulo()
        autor = leerAutor()
        precio = leerPrecio()

        datlib = {
            "Titulo": titulo,
            "Autor": autor,
            "Precio": precio
        }

        lib[cod] = datlib

        pprint.pprint(lib)

        lib = dict(sorted(lib.items()))

        pprint.pprint(lib)

    else:
        print("El código ya existe en la librería.")

    input("Presione cualquier tecla para volver al menu...")
    return lib

def Consultar():
    print("\n\n**2. CONSULTAR ***")
    input("Presione cualquier tecla para volver al menu...")

"""
libreria = {
    codigo1(str): {
        titulo:(str)
        autor:(str)
        precio:int   
    },

    codigo2(str): {
        titulo:(str)
        autor:(str)
        precio:int  
}
"""

def menu():
    while True:
        print("** Librería **")
        print("1. Insertar")
        print("2. Consultar")
        print("3. Salir")

        print(">>> Opcion? ", end="")
        try:
            opcion = int(input())
            if opcion < 1 or opcion > 3:
                print("ERROR. Opción NO válida")
                input("Presione cualquier tecla para volver al menu...")
            return opcion
            
        except ValueError:
            print("ERROR. Opción NO válida")
            input("Presione cualquier tecla para volver al menu...")

# PROGRAMA PRINCIPAL

libreria = {}

while True:
    op = menu()
    match op:
        case 1:
            libreria = Insertar(libreria)
            guardar(libreria)
        case 2:
            Consultar(libreria)
        case 3:
            print("\n\nGracias por usar el software.\n")
            break
