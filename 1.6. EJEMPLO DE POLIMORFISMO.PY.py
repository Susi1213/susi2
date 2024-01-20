# Clase Base
class FiguraGeometrica:
    def __init__(self, nombre, area):
        self.nombre = nombre
        self.area = area

    def calcular_area(self):
        return self.area

# Clase Derivada
class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        super().__init__("Cuadrado", lado * lado)
        self.lado = lado

    def __str__(self):
        return f"Cuadrado con lado {self.lado} y área {self.area}"

# Clase Derivada
class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__("Circulo", 3.14 * radio * radio)
        self.radio = radio

    def __str__(self):
        return f"Circulo con radio {self.radio} y área {self.area}"

# Ejemplo de polimorfismo a través de métodos sobrescritos
def imprimir_area(figura):
    print(f"El área de la figura {figura.nombre} es {figura.calcular_area()}")

imprimir_area(Cuadrado(5))
imprimir_area(Circulo(10))

# Ejemplo de polimorfismo a través de argumentos múltiples/variables
def calcular_area_multiple(figuras):
    for figura in figuras:
        print(f"El área de la figura {figura.nombre} es {figura.calcular_area()}")

figuras = [Cuadrado(5), Circulo(10)]
calcular_area_multiple(figuras)

# Ejemplo de polimorfismo a través de métodos con argumentos variables
def imprimir_figuras(figuras):
    for figura in figuras:
        print(figura)

figuras = [Cuadrado(5), Circulo(10)]
imprimir_figuras(figuras)