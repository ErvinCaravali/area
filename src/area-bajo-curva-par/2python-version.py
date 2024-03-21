from multiprocessing import Process, Array

# Definir la función que representa la curva
def f(x):
    return 4 / (1 + (x * x))

# Función para calcular una porción del área bajo la curva para un proceso específico
def bloque_rectangulos(li, ls, nr, nh, ih, resultado):
    ancho_rectangulo = (ls - li) / nr
    suma_parcial = 0
    for i in range(ih, nr, nh):
        altura_rectangulo = f(li + i * ancho_rectangulo)
        area_rectangulo = altura_rectangulo * ancho_rectangulo
        suma_parcial += area_rectangulo
    resultado[ih] = suma_parcial

#
# PROGRAMA PRINCIPAL
#

# Obtener valores de entrada
X0 = float(input("Ingrese el valor de Xinicial: "))
Xn = float(input("Ingrese el valor de Xfinal: "))
NR = int(input("Ingrese el número de rectángulos: "))
NP = int(input("Ingrese el número de procesos: "))

# Inicializar variables
total_sum = 0  # Cambio de nombre aquí
processes = [] # Lista de procesos
arreglo = Array('f', range(NP)) # Arreglo compartido para almacenar resultados

# Crear los procesos y ejecutar la función bloque_rectangulos en cada uno
for i in range(NP):
    p = Process(target=bloque_rectangulos, args=(X0, Xn, NR, NP, i, arreglo))
    processes.append(p)
    p.start()

# Esperar a que todos los procesos terminen
for process in processes:
    process.join()

# Sumar todas las sumas parciales
total_sum = sum(arreglo)

# Imprimir el resultado
print("El área bajo la curva es:", total_sum)  # Cambio de nombre aquí
