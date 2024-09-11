suma = 0
cant_mult = 0
suma_num = 0
while suma <= 1000:
    N = int(input("Ingrese un número \n"))
    suma += N
    if N % 6 == 0:
        cant_mult += 1
    if N >= 1 and N <= 10:
        suma_num += N
print ("La cantidad de números multiplos de 6 que ingreso el usuario es: ", (cant_mult))
print ("La suma de los Números ingresados por el usuario entre 1 y 10 es: ", (suma_num))


 