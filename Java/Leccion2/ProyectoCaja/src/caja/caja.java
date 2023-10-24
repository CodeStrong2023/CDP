/*
Ejercicio 1: Crear un proyecto segun las especificacion
mostradas a continuacion.
 */
package caja;

public class caja {
    int ancho;
    int alto;
    int profundo;
    
    public caja() {
    }
    
    public caja(int ancho, int alto, int profundo) {
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    } 
    
    public int calcularVolumen() { //Metodo para calcular
        return ancho * alto * profundo;
    }
    
}
