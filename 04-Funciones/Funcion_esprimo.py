# Funcion que reciba un número y devuelva True si es primo o False si no lo es

def esprimo(num):
    if num > 1:
        esprimo = True
        for i in range(2, num):
            if num % i == 0:
                esprimo = False
                break
        
        if esprimo: # Es equivalente a: esprimo == True
            return True
        else:
            return False
        
    else:
        return False
    
# Programa que reciba una serie de número hasta que se ingrese un primo

n = int(input("Número? "))
while not esprimo(n):
    n = int(input("Número? "))
    