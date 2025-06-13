# Importar la clase Te desde el archivo te.py
from te import Te

# Crear dos objetos o instancias de la clase Te
te1 = Te()
te2 = Te()

# Obtener el tipo de dato de cada instancia usando la función type()
tipo1 = type(te1)
tipo2 = type(te2)

# Mostrar en pantalla el tipo de dato de cada objeto
print(f"Tipo de te1: {tipo1}")
print(f"Tipo de te2: {tipo2}")

# Comparar los tipos y mostrar un mensaje correspondiente
if tipo1 == tipo2:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")