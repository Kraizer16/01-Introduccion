import json
import pprint

with open("10-Archivos/Json/datos.json", "r") as fd:
    estructura = json.load(fd)

pprint.pprint(estructura)
print(type(estructura))
