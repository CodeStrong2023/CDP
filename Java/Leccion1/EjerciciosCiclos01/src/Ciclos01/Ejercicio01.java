//Ejercicio 1 : Leer un numero y mostrar su cuadrado, repetir el proceso hasta que se introduzca un numero negativo

package Ciclos01;

import javax.swing.JOptionPane;



public class Ejercicio01 {
   public static void main (String[] args) {
       int numero, cuadrado;
       
       numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un dialogo"));
       while(numero >= 0){ //Mientras el numero sea igual a cero o positivo
           cuadrado =(int)Math.pow(numero, 2);
           System.out.println("El numero "+numero+" elevado al cuadrado es: "+cuadrado);
           numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));    
       }
       System.out.print("El programa a finalizado por numero negativo");
       
       
    } 
}
