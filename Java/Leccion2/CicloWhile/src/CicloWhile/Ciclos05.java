/*Ejercicio 5: Realizar un juego para adivinar un número,
para ello generar un número aleatorio entre 0-100, y
luego ir pidiendo números indicando "es mayor" o
"es menor" según sea mayor o menor con respecto a N
EI proceso termina cuando eI usuario acierta y mostramos
eI número de intentos hechos.
*/
package CicloWhile;

import java.util.Scanner;

public class Ciclos05 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, aleatorio, conteo = 0;
        aleatorio = (int) (Math.random() * 100); // Esto genera un numero alaetorio
        do {
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            if (numero < aleatorio) {
                System.out.println("Digite un numero mayor");
            } else if (numero > aleatorio) {
                System.out.println("Digite un numero menor");
            } else {
                System.out.println("FELICIDADES HAS ADIVINADO EL NUMERO!!");
            }
            conteo++;
        } while (numero != aleatorio);
        System.out.println("Adivinaste el numero en: " + conteo + " intentos");
    }
}
