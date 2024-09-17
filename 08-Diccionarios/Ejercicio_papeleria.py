articulos = {1:"Lapiz", 2:"Cuadernos", 3:"Borrador", 4:"Calculadora"
             , 5:"Escuadra" }

valores = {1:2500, 2:3800, 3:1200, 4:35000, 5:3700}

print("")
print("Bienvenido\n".center(40))
print("-" * 30, "\n")   
print("Cual de los siguientes articulos desea comprar: ")
digit = 0
for k in articulos.keys():
 digit += 1
 print(k, articulos[digit], ":" " $", valores[digit])
print("-" * 30, "\n")  
digitA = int(input("Ingrese el codigo del articulo que desa comprar: \n"))

digitC = int(input("Ingrese la cantidad de articulos que desea comprar: \n"))


suma = valores[digitA] * digitC
print(">> FACTURA <<".center(40))
print("-" * 30, "\n") 
print("Usted ha comprado ", digitC, articulos[digitA], "con un precio unitario de: $"
      , valores[digitA])
print("-" * 30, "\n") 
print("El total de su compra es: \n $", suma)
print("-" * 30, "\n") 
print(">> Hasta luego, Vuelva pronto <<\n".center(40))
