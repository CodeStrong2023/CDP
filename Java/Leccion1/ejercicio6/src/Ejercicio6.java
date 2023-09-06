
import java.util.Scanner;

public class Ejercicio6 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float guillermo,luis,juan,total;
        System.out.println("digitar la cantidad de dinero que tiene guillermo");
        guillermo = Float.parseFloat(entrada.nextLine());
        
        luis = guillermo / 2;
        juan = (luis + guillermo) / 2;
        total = luis + guillermo + juan;
        System.out.println("\nEl dinero de luis es: US$"+luis);
        System.out.println("el dinero de juan es: US$"+juan);
        System.out.println("el total de dinero entre los 3 es: US$"+total);
        
        
    }
    
}
