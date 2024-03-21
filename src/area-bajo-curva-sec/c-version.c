#include <stdio.h>

// Definir la función que representa la curva
double f(double x) {
    // Ejemplo: f(x) = 4 / (1 + x^2)
    return 4 / (1 + (x * x));
}

// Función para calcular el área bajo la curva utilizando rectángulos
double calcular_area_bajo_curva(double x_inicial, double x_final, int num_rectangulos) {
    // Determinar cuál es el ancho del rectángulo y guardarlo en una variable
    double ancho_rectangulo = (x_final - x_inicial) / num_rectangulos;
    
    // Inicializar la variable para almacenar el área total
    double area_total = 0;
    
    // Hacer un ciclo que calcule el área de todos los rectángulos y vaya sumando
    for (int i = 0; i < num_rectangulos; i++) {
        double altura_rectangulo = f(x_inicial + i * ancho_rectangulo);
        double area_rectangulo = altura_rectangulo * ancho_rectangulo;
        area_total += area_rectangulo;
    }
    
    return area_total;
}

int main() {
    double x_inicial, x_final;
    int num_rectangulos;

    // Solicitar al usuario que ingrese los datos
    printf("Ingrese el valor de Xinicial: ");
    scanf("%lf", &x_inicial);
    printf("Ingrese el valor de Xfinal: ");
    scanf("%lf", &x_final);
    printf("Ingrese el número de rectángulos: ");
    scanf("%d", &num_rectangulos);

    // Calcular el área bajo la curva utilizando la función definida
    double area_resultante = calcular_area_bajo_curva(x_inicial, x_final, num_rectangulos);

    // Imprimir el resultado
    printf("El área bajo la curva es: %.10lf\n", area_resultante);

    return 0;
}
