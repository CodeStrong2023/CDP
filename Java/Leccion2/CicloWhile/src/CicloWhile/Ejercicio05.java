/*Ejercicio 5: Realizar un juego para adivinar un número,
para ello generar un número aleatorio entre 0-100, y
luego ir pidiendo números indicando "es mayor" o
"es menor" según sea mayor o menor con respecto a N
EI proceso termina cuando eI usuario acierta y mostramos
eI número de intentos hechos.
*/
package CicloWhile;

import javax.swing.JOptionPane;

public class Ejercicio05 {
    public static void main(String[] args) {
        int numero, aleatorio, conteo = 0;
        aleatorio = (int) (Math.random() * 100); // Esto genera un numero alaetorio
        do {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            if (numero < aleatorio) {
                JOptionPane.showMessageDialog(null, "Digite un numero mayor");
            } else if (numero > aleatorio) {
                JOptionPane.showMessageDialog(null, "Digite un numero menor");
            } else {
                JOptionPane.showMessageDialog(null, "FELICIDADES HAS ADIVINADO EL NUMERO!!");
            }
            conteo++;
        } while (numero != aleatorio);
        JOptionPane.showMessageDialog(null, "Adivinaste el numero en: " + conteo + " intentos");
    }
}
