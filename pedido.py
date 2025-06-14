from te import Te

print("=== Sistema de Pedidos de Té ===")
print("Seleccione el sabor:")
print("1: Té negro\n2: Té verde\n3: Agua de hierbas")

sabor = int(input("Ingrese el número correspondiente al sabor: "))
formato = int(input("Ingrese el formato (300 o 500 gramos): "))

# Obtener tiempo y recomendación
resultado_preparacion = Te.obtener_preparacion_y_recomendacion(sabor)
precio = Te.obtener_precio(formato)

# Validar resultados antes de continuar
if resultado_preparacion is None:
    print("\nError: Sabor no válido. Debe ser 1, 2 o 3.")
elif precio is None:
    print("\nError: Formato no válido. Solo se aceptan 300 o 500 gramos.")
else:
    tiempo, recomendacion = resultado_preparacion
    sabores = {1: "Té negro", 2: "Té verde", 3: "Agua de hierbas"}

    print("\n=== Detalle del Pedido ===")
    print(f"Sabor: {sabores[sabor]}")
    print(f"Formato: {formato} gr")
    print(f"Precio: ${precio}")
    print(f"Tiempo de preparación: {tiempo} minutos")
    print(f"Recomendación: {recomendacion}")