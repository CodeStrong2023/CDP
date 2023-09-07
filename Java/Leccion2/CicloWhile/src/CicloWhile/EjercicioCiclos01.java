// Ejercicio1: Leer un numero y mostrar su cuadrado,repetir el proceso hasta que se introduzca un numero negativos
package CicloWhile;

import java.util.Scanner;

public class EjercicioCiclos01 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int numero, cuadrado;
        System.out.println("digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while (numero >= 0) { // Mientras el numero sea igual a cero o positivo
            cuadrado = (int) Math.pow(numero, 2);
            System.out.println("El numero " + numero + " elvado al cuadrado es: " + cuadrado);
            System.out.println("digite otro numero");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El programa a finalizado por numero negativo");
    }

}
