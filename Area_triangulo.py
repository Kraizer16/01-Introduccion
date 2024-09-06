# Dado la base y la altura de un triángulo y mostrar su área, a traves de la
# fórmuka área = (base * altura) / 2

# ENTRADA
# b: base : float
# h: altura : float

b = float(input("Introduzca la base del Triángulo: "))
h = float(input("Introduzca la altura del triángulo: "))

a = b * h / 2

# Formateando la salida con format()
print("El área del triángulo es: {:.1f}".format(a))

# Formateando la salida con cadenas f-string
print(f"El área del triángulo es: {a:.1f}")

# Proceso
# a = b * h / 2

#SALIDA
# a: área : float