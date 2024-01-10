# Programa: Calculadora de Área de Rectángulo
# Descripción: Este programa calcula el área de un rectángulo dado su ancho y altura.

# Función para calcular el área del rectángulo
def calcular_area_rectangulo(ancho, altura):
    """
    Calcula el área de un rectángulo.

    :param ancho: Ancho del rectángulo (float o int)
    :param altura: Altura del rectángulo (float o int)
    :return: Área del rectángulo (float)
    """
    area = ancho * altura
    return area

# Entrada de datos desde el usuario
ancho_rectangulo = float(input("Ingrese el ancho del rectángulo: "))
altura_rectangulo = float(input("Ingrese la altura del rectángulo: "))

# Llamada a la función para calcular el área
area_resultante = calcular_area_rectangulo(ancho_rectangulo, altura_rectangulo)

# Mostrar el resultado
print(f"El área del rectángulo con ancho {ancho_rectangulo} y altura {altura_rectangulo} es: {area_resultante}")