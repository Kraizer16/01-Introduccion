
num1 = int(input("Ingrese el primer número entero: \n"))
num2 = int(input("Ingrese el segundo números entero: \n"))
num3 = int(input("Ingrese el tercer número entero: \n"))
print ("")
print ("El orden de los números de mayor a menor es:")
if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print (num1)
        print (num2)
        print (num3)
    else:  
        print (num1)
        print (num3)
        print (num2)
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        print (num2)
        print (num1)
        print (num3)
    else:
        print (num2)
        print (num3)
        print (num1)
elif num3 >= num1 and num3 >= num2:
    if num1 >= num2:
        print (num3)
        print (num1)
        print (num2)
    else:
        print (num3)
        print (num2)
        print (num1)


