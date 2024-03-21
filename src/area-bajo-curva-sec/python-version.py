# Definir la función que representa la curva
def f(x):
    # Ejemplo: f(x) = x^2
    return 4 / (1 + (x * x))

# Función para calcular el área bajo la curva utilizando rectángulos
def calcular_area_bajo_curva(x_inicial, x_final, num_rectangulos):
    # Determinar cuál es el ancho del rectángulo y guardarlo en una variable
    ancho_rectangulo = (x_final - x_inicial) / num_rectangulos
    
    # Inicializar la variable para almacenar el área total
    area_total = 0
    
    # Hacer un ciclo que calcule el área de todos los rectángulos y vaya sumando
    for i in range(num_rectangulos):
        altura_rectangulo = f(x_inicial + i * ancho_rectangulo)
        area_rectangulo = altura_rectangulo * ancho_rectangulo
        area_total += area_rectangulo
    
    return area_total

x_inicial = float(input("Ingrese el valor de Xinicial: "))
x_final = float(input("Ingrese el valor de Xfinal: "))
num_rectangulos = int(input("Ingrese el número de rectángulos: "))

area_resultante = calcular_area_bajo_curva(x_inicial, x_final, num_rectangulos)

# Imprimir el resultado
print("El área bajo la curva es:", area_resultante)

