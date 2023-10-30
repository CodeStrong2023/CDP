import java.util.Scanner;

public class lodepipojava.java
{

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[][] matriz = new int[9][3];
        int[][] matriz1 = new int[10][8];
        int[] arreglo = new int[9];
        double cuenta = 0;
        int opcion;
        int mesa;
        int pedido;
        boolean repite;
        int cp;
        int mp = 900;
        int mpf = 950;
        int hc = 670;
        int hco = 800;
        int a = 250;
        int cc = 350;
        int as = 300;
        int ca = 800;
        int p1 = 0;
        int p2 = 0;
        int p3 = 0;
        int p4 = 0;
        int p5 = 0;
        int p6 = 0;
        int p7 = 0;
        int p8 = 0;
        int caja = 0;

        for (int i = 0; i < 9; i++) {
            arreglo[i] = 0;
        }

        do {
            System.out.println("Restaurante: A LO DE PIPO");
            System.out.println("MENU");
            System.out.println("1. Agregar mesa");
            System.out.println("2. Imprimir Cuenta");
            System.out.println("3. Eliminar Mesa");
            System.out.println("4. Cerrar Caja");
            System.out.println("5. Salir");
            opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    System.out.println("Indique la mesa");
                    mesa = scanner.nextInt();
                    repite = true;
                    cuenta = 0;
                    p1 = 0;
                    p2 = 0;
                    p3 = 0;
                    p4 = 0;
                    p5 = 0;
                    p6 = 0;
                    p7 = 0;
                    p8 = 0;

                    do {
                        System.out.println("Seleccione el pedido");
                        System.out.println("----------------------CARTA----------------------");
                        System.out.println("1. Milanesa napolitana con pure--------------$900");
                        System.out.println("2. Milanesa napolitana con papas fritas------$950");
                        System.out.println("3. Hamburguesa clasica-----------------------$670");
                        System.out.println("4. Hamburguesa completa----------------------$800");
                        System.out.println("---------------------BEBIDAS---------------------");
                        System.out.println("5. Agua mineral 500ml------------------------$250");
                        System.out.println("6. Coca Cola 500ml---------------------------$350");
                        System.out.println("7. Agua saborizada 500ml---------------------$300");
                        System.out.println("8. Cerveza Andes 1L--------------------------$800");
                        System.out.println("0. Regresar");
                        pedido = scanner.nextInt();

                        switch (pedido) {

                        }
                    } while (repite);
            }
        } while (opcion != 5);
    }
}