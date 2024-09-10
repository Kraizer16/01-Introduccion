# Ingreso de datos

codigo = input("Ingrese su código: \n")
Nombre = input("Ingrese su nombre: \n")
Estado = input("Ingrese su Estado actual, Puede ser Vigente(V) o Suspedido(S) \n")
Estrato = int(input("Ingrese su estrato, Puede ser del uno (1) al seis (6) \n"))
Consumo = int(input("Ingrese su consumo en el mes, En centímetros cúbicos (cm³) \n"))


Estrato1 = 10_000
Estrato2 = 20_000
Estrato3 = 30_000
Estrato4 = 45_000
Estrato5 = 60_000
Estrato6 = 70_000

sumaC = Consumo * 200

if Estrato == 1:
    SumaT = Estrato1 + sumaC
    print("El nombre del usuario es: /n" (Nombre))
    print("El valor de la tarifa básica es: /n" (Estrato1))
    print("El valor del consumo es: /n" (sumaC))
    