def juicio(definitiva):
   if definitiva >= 60:
      return True
   else:
      return False
    
   

n = int(input("Ingrese la cantidad de estudiantes: \n"))
Estudiantes = {}

for i in range(n):
    print(f"\nEstudiante{i+1}")
    codigo = int(input("Codigo?\n"))
    dDatos = {}
    if codigo == 999:
        break
    else:
     dDatos["Nombre"] = input("Nombre? \n")
     dDatos["Nota1"] = int(input("Nota1? (0 - 100) \n"))
     dDatos["Nota2"] = int(input("Nota2? (1 - 5) \n"))
     dDatos["Nota3"] = int(input("Nota3? (1 - 5) \n"))
     dDatos["Definitiva"] = int(f"{(dDatos["Nota1"] * 0.30) + (dDatos["Nota2"] * 0.30) + (dDatos["Nota3"] * 0.40):.0f}")
     Estudiantes[codigo] = dDatos


print(Estudiantes)
for k in Estudiantes.keys():
 if juicio(Estudiantes[k]["Definitiva"]):
    print("El estudiante: ", Estudiantes[k]["Nombre"], " ha aprobado")
 else:
    print("El estudiante", Estudiantes[k]["Nombre"], " ha desaprobado")





