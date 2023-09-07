package CicloWhile;

import javax.swing.JOptionPane;

public class Ejercicio01 {
    public static void main(String[] args) {

        int numero, cuadrado;

        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while (numero >= 0) { // Mientras el numero sea igual a cero o positivo
            cuadrado = (int) Math.pow(numero, 2);
            System.out.println("El numero " + numero + " elvado al cuadrado es: " + cuadrado);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        System.out.println("El programa a finalizado por numero negativo");
    }

}
