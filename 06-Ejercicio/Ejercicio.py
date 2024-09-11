# Solicitar al usuario que ingrese un número entero N,
# luego generar en forma aleatoria N números enteros comprendidos
# entre 1 y 100 y determinar cuántos son pares y cuántos impares.

# Se importa la libreria random
import random

# Se Pregunta al usario un Número N
N = int(input("Ingrese un número \n"))

# Se realiza un ciclo for que se repita N veces
for i in range (0, N):
 
 # Se crea una variable donde se va a almacenar el numero aleatorio
 # Entre 1 y 100
 NumAzar = random.randint(1, 100)
 
 print("=" * 40, "\n")

 # Se crea una condicional para evaluar si es "PAR" o "IMPAR"
 if NumAzar % 2 == 0:
  
 # Imprime si el numero al azar es Par
  print ("El Número: ", (NumAzar) , " : Es Par")

  print("=" * 40, "\n")
  
 else:
  
 # Imprime si el numero al azar es Impar
  print ("El Número: ", (NumAzar) , " : Es impar")

  print("=" * 40, "\n")