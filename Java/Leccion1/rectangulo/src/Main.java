
public class Main {

    public static void main(String[] args) {
        //Calcular el area y el perimetro de un rectangulo
        double longitud = 5.0;
        double ancho = 3.0;

        double area = longitud * ancho;
        double perimetro = 2 * (longitud + ancho);

        System.out.println("area del rectangulo: " + area);
        System.out.println("Perimetro del rectangulo: " + perimetro);

        //Comparar dos numeros y encontrar el mayor utilizando el operador ternario
        int numero1 = 10;
        int numero2 = 7;

        int mayor = (numero1 > numero2) ? numero1 : numero2;

        System.out.println("El numero mayor es: " + mayor);
 
    }
}
