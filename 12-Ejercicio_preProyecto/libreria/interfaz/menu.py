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