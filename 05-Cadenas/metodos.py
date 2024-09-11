#.strip([chars]): Elimina los caracteres al principio y al final de la cadena.
# Si no se especifica chars, se eliminan espacios en blanco.
cadena = "  hola  "
print(cadena.strip())  # 'hola'

#.lower(): Convierte todos los caracteres de la cadena a minúsculas.
cadena = "Hola Mundo"
print(cadena.lower())  # 'hola mundo'

#.upper(): Convierte todos los caracteres de la cadena a mayúsculas.
cadena = "Hola Mundo"
print(cadena.upper())  # 'HOLA MUNDO'

#.capitalize(): Convierte el primer carácter de la cadena a mayúscula y el resto a minúsculas.
cadena = "hola mundo"
print(cadena.capitalize())  # 'Hola mundo'

#.title(): Convierte el primer carácter de cada palabra en mayúscula y el resto en minúsculas.
cadena = "hola mundo"
print(cadena.title())  # 'Hola Mundo'

#.replace(old, new[, count]): Reemplaza las ocurrencias de old con new.
# Opcionalmente, puedes especificar el número máximo de reemplazos con count.
cadena = "hola mundo"
print(cadena.replace("mundo", "Python"))  # 'hola Python'

#.find(sub[, start[, end]]): Devuelve el índice de la primera aparición de sub dentro de la cadena, o -1 si no se encuentra.
# Puedes especificar el rango de búsqueda con start y end.
cadena = "hola mundo"
print(cadena.find("mundo"))  # 5

#.rfind(sub[, start[, end]]): Similar a .find(), pero busca la última aparición de sub.
cadena = "hola mundo mundo"
print(cadena.rfind("mundo"))  # 11

#.split([sep[, maxsplit]]): Divide la cadena en una lista usando sep como delimitador. Puedes limitar el número de divisiones con maxsplit.
cadena = "hola mundo Python"
print(cadena.split())  # ['hola', 'mundo', 'Python']

#.join(iterable): Une los elementos de un iterable (como una lista) en una cadena usando la cadena actual como delimitador.
lista = ["hola", "mundo", "Python"]
print(" ".join(lista))  # 'hola mundo Python'

#.startswith(prefix[, start[, end]]): Comprueba si la cadena comienza con el prefijo prefix. Puedes especificar un rango de búsqueda con start y end.
cadena = "hola mundo"
print(cadena.startswith("hola"))  # True

#.endswith(suffix[, start[, end]]): Comprueba si la cadena termina con el sufijo suffix. Puedes especificar un rango de búsqueda con start y end.
cadena = "hola mundo"
print(cadena.endswith("mundo"))  # True

#.format(*args, **kwargs): Permite formatear cadenas utilizando {} como placeholders.
nombre = "Juan"
edad = 30
cadena = "Mi nombre es {} y tengo {} años".format(nombre, edad)
print(cadena)  # 'Mi nombre es Juan y tengo 30 años'

#.zfill(width): Rellena la cadena con ceros a la izquierda hasta alcanzar el ancho width.
cadena = "42"
print(cadena.zfill(5))  # '00042'