# Encontrar si un número es narcisista o no?
# Encontrar si la suma de sus dígitos elevado a la cantidad de dígitos es igual al número
# ejemplo:
# 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 123

# paso 1 - pedir el número
import math


n = int(input("Ingrese el número \n"))
if n > 0:
    # paso 2 = calcular la longitud del número
    lnum = int(math.log10(n)) 

    # paso 3 = sacar los dígitos del número y sumarlos elevandolos a la longitud del número
    suma = 0
    temp = n
    for i in range(1, lnum +1):
        d = n % 10 
        suma += d ** lnum
        n = n // 10

    if suma == temp:
        print("El número es narciso")
    else:
        print("El número no es narciso")
else:
    print("ERROR. Ingrese un número entero positivo")