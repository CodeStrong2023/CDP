/*

 */
package test;

public class PruebaPersona {
    public static void main(String args[]){
        Persona persona1 = new persona("Mica", 57.000, false);
        
        //Modificar a traves de los metodos 
        persona1.setNombre("Antonella");
        //persona1.nombre="Antonella";//Ya no se puede utilizar
        //System.out.println("Nombre es: "+persona1.nombre);//Error
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
    }
    
}
