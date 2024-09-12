def imprimeLista(lst):
    for e in lst:
        print(e, end = " | ")

n = int(input("Cuantas letras va a ingresar \n"))

lstVocales = [0] * 5

for i in range(n):
    letra = input(f"Ingrese la letra {i + 1}: \n")

    letra = letra.strip()
    if len(letra[0]) > 0:
        letra = letra[0].lower()
        # if letra.lower() == "a":
        #     lstVocales[0] += 1
        # elif letra.lower() == "e":
        #     lstVocales[1] += 1
        # elif letra.lower() == "i":
        #     lstVocales[2] += 1
        # elif letra.lower() == "o":
        #     lstVocales[3] += 1
        # elif letra.lower() == "u":
        #     lstVocales[4] += 1
        match letra:
         case "a":
          lstVocales[0] += 1
         case "e":
          lstVocales[1] += 1
         case "i":
          lstVocales[2] += 1
         case "o":
          lstVocales[3] += 1
         case "u":
          lstVocales[4] += 1
         case _:
          pass






imprimeLista(lstVocales)
