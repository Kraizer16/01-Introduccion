from os import wait
from turtle import clearscreen



def menu():
    print(">> MENÚ <<")
    print("")
    print ("1. El primer item de la lista de Reinos")
    print ("")
    print("2. El ultimo item de la lista de Reinos")
    print ("")
    print ("3. La lista (Bacteria, Protozoa, Chromista)")
    print (" ")
    print ("4. La lista (Chromista, Plantae, Fungi)")
    print (" ")
    print ("5. La lista (fungi, Animalia)")
    print (" ")
    print ("6. Lista Vacía")
    print (" ")
    print ("7. Salir")
    print (" ")
    print (">> ¿Opción? >>")

def firstItem(lst):
    primerElemento = lst[0]
    return primerElemento



kingdoms = ["Bacteria", "Protozoa", "Chromista", "Plantae", "Fungi", "Animalia"]

sw = True
while sw:
    clearscreen

    print(menu())
    opcion = int(input("Ingrese la opción a la que desea Ingresar: \n"))
    match opcion:
        case 1:
            print ("1. El primer item de la lista de Reinos")
            print ("")
            print("el primer elemento de la lista es: ", firstItem(kingdoms))
            print("")
            print("Presione cualquier tecla para voler al menú...")
            wait

