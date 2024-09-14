d_categoria = {1:25_000, 2:30_000, 3:40_000, 4:45_000
               , 5:60_000}
# Devuelve las llaves y los valores 
print(d_categoria.items())
for k, v in d_categoria.items():
    print(k, v)

# Elimina la llave con su valor
d_categoria.pop(4)
print(d_categoria)

# imprime los valores del dicciocario
for v in d_categoria.values():
    print(v)