
from modelo.modelo import Insertar, Consultar
from interfaz.menu import menu
from persistencia.persistencia import cargar

# PROGRAMA PRINCIPAL

libreria = {}
archivo = "12-Ejercicio_preProyecto/libreria/libreria.json"
libreria = cargar(archivo)

print(libreria)

while True:
    op = menu()
    match op:
        case 1:
            libreria = Insertar(libreria, archivo)   
        case 2:
            Consultar(libreria)
        case 3:
            print("\n\nGracias por usar el software.\n")
            break
