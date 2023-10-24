/*
Ejercicio 1: Crear un proyecto segun las especificacion
mostradas a continuacion.
 */
package caja;

public class PruebaCaja {
    public static void main(String args[]){
        int medidaAncho = 3;
        int medidaAlto = 2;
        int medidaProf = 6;
        
        caja caja1 = new caja();
        caja1.ancho = medidaAncho;
        caja1.alto =medidaAlto;
        caja1.profundo = medidaProf;
        int resultado = caja1.calcularVolumen();
        
        System.out.println("resultado volumen de caja 1:" + resultado);
        
        caja caja2 = new caja(2, 4, 6);
        
        System.out.println("resultado volumen de caja 2:" + caja2.calcularVolumen());
    }
}
