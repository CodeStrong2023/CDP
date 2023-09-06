import java.util.Scanner;

public class Ejercicio5 {
    public static void main(String[] args) {
        // Crear un objeto Scanner para leer la entrada del usuario
        Scanner entrada = new Scanner(System.in);

        // Pedir al usuario que ingrese las calificaciones
        System.out.println("Ingrese la primera calificación: ");
        double calificacion1 = entrada.nextDouble();

        System.out.println("Ingrese la segunda calificación: ");
        double calificacion2 = entrada.nextDouble();

        System.out.println("Ingrese la tercera calificación: ");
        double calificacion3 = entrada.nextDouble();

        // Calcular la suma de las calificaciones
        double sumaCalificaciones = calificacion1 + calificacion2 + calificacion3;

        // Imprimir la suma de las calificaciones
        System.out.println("La suma de las calificaciones es: " + sumaCalificaciones);

        
    }
}

