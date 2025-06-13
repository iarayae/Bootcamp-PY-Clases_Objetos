# Definición de la clase principal "Te"
class Te:
    # Atributo de clase: duración estándar de todos los tés (en días)
    duracion = 365

    @staticmethod
    def obtener_preparacion_y_recomendacion(sabor):
        """
        Retorna el tiempo de preparación y la recomendación de consumo
        según el tipo de sabor seleccionado (1, 2 o 3).
        """
        if sabor == 1:
            return 3, "Se recomienda consumir al desayuno"
        elif sabor == 2:
            return 5, "Se recomienda consumir al medio día"
        elif sabor == 3:
            return 6, "Se recomienda consumir al atardecer"

    @staticmethod
    def obtener_precio(formato):
        """
        Retorna el precio del té según el formato (300g o 500g).
        """
        if formato == 300:
            return 3000
        elif formato == 500:
            return 5000