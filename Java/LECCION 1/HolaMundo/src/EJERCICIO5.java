
import static java.time.Clock.system;

public class EJERCICIO5 {
    public static void main (String [] args) {
     scanner entrada = new scanner (System.in);
     float nota1,nota2,nota3,suma;
     system.out.println("digite las tres calificaciones: ");
     nota1 = float.parsefloat (entrada . nextline());
     nota2 = float.parsefloat (entrada . nextline());
     nota3 = float.parsefloat (entrada . nextline());
     suma = nota1 + nota2 + nota3;
     system.out.println("\nla suma es: "+suma);
    }
}
