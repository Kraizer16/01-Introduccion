#import pprint

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
from persistencia.persistencia import guardar

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



def Insertar(lib, arch):
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

        # pprint.pprint(lib)
        lib = dict(sorted(lib.items()))
        # pprint.pprint(lib)

        guardar(lib, arch)

    else:
        print("El código ya existe en la librería.")

    input("Presione cualquier tecla para volver al menu...")
    return lib

def Consultar(lib):
    print("\n\n**2. CONSULTAR ***")

    cod = input("\nCódigo del libro? ")

    if cod in lib:
        print("-> Código", cod)

        print(f"-> Titulo: {lib[cod]['Titulo']}")
        print(f"-> Autor: {lib[cod]['Autor']}")
        print(f"-> Precio: ${lib[cod]['Precio']:,.0f}")
    else:
        print(">>> Error. El codigo del libro no existe en la libreria")


    input("Presione cualquier tecla para volver al menu...")