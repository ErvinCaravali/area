#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define NUM_THREADS 4

// Definir la función que representa la curva
double f(double x) {
    // Ejemplo: f(x) = x^2
    return 4 / (1 + (x * x));
}

// Estructura para los argumentos de la función del hilo
struct thread_args {
    double x_inicial;
    double x_final;
    int num_rectangulos;
    int num_hilos;
    int id_hilo;
    double resultado_parcial;
};

// Función para calcular el área bajo la curva en un rango específico
void *calcular_area_parcial(void *args_void) {
    struct thread_args *args = (struct thread_args *)args_void;
    
    double width = (args->x_final - args->x_inicial) / args->num_rectangulos;
    double sum_local = 0;
    
    for (int i = args->id_hilo; i < args->num_rectangulos; i += args->num_hilos) {
        double x = args->x_inicial + i * width;
        double height = f(x);
        sum_local += width * height;
    }
    
    args->resultado_parcial = sum_local;
    
    pthread_exit(NULL);
}

// PROGRAMA PRINCIPAL
int main() {
    double X0, Xn;
    int NR, NH;

    printf("Ingrese el valor de Xinicial: ");
    scanf("%lf", &X0);

    printf("Ingrese el valor de Xfinal: ");
    scanf("%lf", &Xn);

    printf("Ingrese el número de rectángulos: ");
    scanf("%d", &NR);

    printf("Ingrese el número de hilos: ");
    scanf("%d", &NH);

    pthread_t threads[NUM_THREADS];
    struct thread_args args[NUM_THREADS];
    
    // Crear y ejecutar los hilos
    for (int i = 0; i < NUM_THREADS; i++) {
        args[i].x_inicial = X0;
        args[i].x_final = Xn;
        args[i].num_rectangulos = NR;
        args[i].num_hilos = NH;
        args[i].id_hilo = i;
        
        pthread_create(&threads[i], NULL, calcular_area_parcial, (void *)&args[i]);
    }
    
    // Esperar a que los hilos terminen
    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }
    
    // Calcular el área total sumando los resultados parciales
    double area_total = 0;
    for (int i = 0; i < NUM_THREADS; i++) {
        area_total += args[i].resultado_parcial;
    }
    
    printf("Área total calculada: %lf\n", area_total);

    return 0;
}
