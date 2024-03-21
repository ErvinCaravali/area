import threading

# Definir la función que representa la curva
def f(x):
    # Ejemplo: f(x) = x^2
    return 4 / (1 + (x * x))

# FUNCION
def bloque_rectangulos(li, ls, nr, nh, ih):
    # Calcula el ancho de cada rectángulo
    width = (ls - li) / nr
    
    # Calcula el área de los rectángulos asignados a este hilo
    sum_local = 0
    for i in range(ih, nr, nh):  # Asegura que cada hilo procese rectángulos alternos
        x = li + i * width  # Calcula la posición x para este rectángulo
        height = f(x)  # Calcula la altura de la curva en la posición x
        sum_local += width * height  # Calcula el área del rectángulo y lo suma
        
    # Almacena el resultado parcial en la lista compartida
    sum_parcial[ih] = sum_local

# PROGRAMA PRINCIPAL
X0 = float(input("Ingrese el valor de Xinicial: "))  # Xinicial
Xn = float(input("Ingrese el valor de Xfinal: "))     # Xfinal
NR = int(input("Ingrese el número de rectángulos: ")) # Número de Rectángulos
NH = int(input("Ingrese el número de hilos: "))       # Número de hilos
threads = []  # Lista con los hilos que llevarán a cabo el procesamiento

# Inicializa la lista de resultados parciales
sum_parcial = [0] * NH

# Crea y comienza los hilos
for i in range(NH):
    thread = threading.Thread(target=bloque_rectangulos, args=(X0, Xn, NR, NH, i))
    thread.start()
    threads.append(thread)

# Espera a que todos los hilos terminen su ejecución
for thread in threads:
    thread.join()

# Calcula la suma total de todas las áreas parciales
total_sum = sum(sum_parcial)
print(f"Área total calculada: {total_sum}")
