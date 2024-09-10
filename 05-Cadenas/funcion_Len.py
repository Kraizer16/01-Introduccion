# Crear una funcion si una contraseña
# es aceptable cuando:
# - Tenga de 3 a 20 caracteres

def validContrasena(contra):
    longContra = len(contra)
    if longContra >= 3 and longContra <= 20:
        return True
    else:
        return False

# Programa que valide una contraseña

passw = input("Contraseña: ")
while not validContrasena(passw):
    passw = input("Contraseña: ")

print("Ingreso ...")