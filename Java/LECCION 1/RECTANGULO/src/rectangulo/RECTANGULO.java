package rectangulo;

import java.util.Scanner;

public class RECTANGULO {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Ingresa la longitud del lado 1: ");
            double lado1 = scanner.nextDouble();
            
            System.out.print("Ingresa la longitud del lado 2: ");
            double lado2 = scanner.nextDouble();
            
            double area = calcularArea(lado1, lado2);
            double perimetro = calcularPerimetro(lado1, lado2);
            
            System.out.println("El área del rectángulo es: " + area);
            System.out.println("El perímetro del rectángulo es: " + perimetro);
        }
    }

    public static double calcularArea(double lado1, double lado2) {
        return lado1 * lado2;
    }

    public static double calcularPerimetro(double lado1, double lado2) {
        return 2 * (lado1 + lado2);
    }
}