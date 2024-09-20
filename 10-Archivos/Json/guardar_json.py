import json

# lista = ["Daniel", "Maria", "Ada", "Julian", "Gabriel", 
#         ["julian", "Ricardo"]]

campers = {

    1:{
        "nombre": "Daniel",
        "edad": 21,
        "sexo": "m",
        "Telefonos": [123, 456]
    },

    2:{
        "nombre": "Maria",
        "edad": 20,
        "sexo": "f",
        "Telefonos": [789] 
    } 

}
with open("10-Archivos/Json/datos.json", "w") as fd:
    json.dump(campers, fd)

if not fd.closed: # True si el archivo esta cerrado
    fd.close