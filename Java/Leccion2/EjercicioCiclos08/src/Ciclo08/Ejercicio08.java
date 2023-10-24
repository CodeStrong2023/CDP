/*
Ejercicio8: Pedir un numero N, y mostrar todos los numeros
de 1 al N.
 */
package Ciclo08;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ejercicio08 {
    public static void main(String[] args){
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        int i = 1;
        while( i <= numero){
            JOptionPane.showMessageDialog(null, 1);
            i++;
        }
    }   
}
