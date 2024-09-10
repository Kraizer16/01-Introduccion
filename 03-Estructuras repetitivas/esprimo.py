# Indicar si un número es primo

num = int(input("Número= \n"))

if num > 1:
    esprimo = True
    for i in range(2, num):
        if num % i == 0:
            esprimo = False
            break
    
    if esprimo: # Es equivalente a: esprimo == True
        print("Es primo")
    else:
        print("No es primo")
else:
    print("No es primo")