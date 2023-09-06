
import java.util.Scanner;

public class HolaMundo {

    public static void main(String[] args) {


        /*System.out.println("Hola Mundo desde java");
        
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        
        //Tipo String
        
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "sigamos creciendo en programacion";
        System.out.println(miVariableCadena);
         */
        //Var - inferencia de tipo en java
        /* var miVariableEntera2 = 10;
        var miVariableCadena2 = "seguimos estudiando";
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        //sout + tab 
        //para ejecutar shif f6
        //regrlas para definir una variab le ne java

        var usuario = "Matias";
        var titulo = "programador";
        var union = titulo + " " + usuario;
        System.out.println("union = " + union);
         */
 /*var a = 8;
        var b = 4;
        System.out.println(a + b);
        //Ejercicio: caracteres especiales con java

        var nombre = "Natalia";
        System.out.println("nueva linea: \n" + nombre); //diagonal inversa y letra n
        System.out.println("tabulador: \t" + nombre); //diagonal inversa y letra t (espacio para centrar)
        System.out.println("\t\t: MENU:.");
        System.out.println("Retroseso: \b\b"+ nombre); //caracter de retroseso
        System.out.println("Comillas simples: \'"+nombre+"\'"); //comillas simples
        System.out.println("Comillas dobles: \""+nombre+"\""); //comillas dobles
         */
        //clase Scanner
        /*Scanner entrada = new Scanner(System.in);
        System.out.println("digite su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: "+titulo2+" "+usuario2);
         */
        //clase 4 3.2
        /*byte numEnteroByte = 127;
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("valor minimo del byte: "+ Byte.MIN_VALUE);
        System.out.println("valor maximo del byte: "+ Byte.MAX_VALUE);
        
        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("valor minimo del short: "+Short.MIN_VALUE);
        System.out.println("valor maximo del short: "+Short.MAX_VALUE);
        
        int numEnteroInt = 10;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("valor minimo del int: "+Integer.MIN_VALUE);
        System.out.println("valor maximo del int: "+Integer.MAX_VALUE);
        
        long numEnteroLong = 10;
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor minimo del long: "+Long.MIN_VALUE);
        System.out.println("Valor maximo del long: "+Long.MAX_VALUE);
         */
        // CLASE 4 3.3
        /* float numFloat = 3.4028235E38F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("El valor minimo del float: " + Float.MIN_VALUE);
        System.out.println("El valor maximo del float: " + Float.MAX_VALUE);

        double numDouble = 1.7976931348623157E308D;
        System.out.println("numDouble = " + numDouble);
        System.out.println("El valor minimo del Double: " + Double.MIN_VALUE);
        System.out.println("El valor maximo del Double: " + Double.MAX_VALUE);
         */
        //CLASE 5 5.1
        //interferencia de tipos var y tipos primitivos
        /*var numEntero = 20; //las literales sin punto automaticamente son te tipo int
        System.out.println("numEntero = " + numEntero);
        var numFloat =10.0F;//autoimaticamente con el punto se transforma en tipo double
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0; 
        System.out.println("numDouble = " + numDouble);
         */
        //tipos primitivos 5.2
        /*
        char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);

        char varCaracter = '\u0024';    //indicamos a java la asignacion con el codigo unicode
        System.out.println("varCaracter = " + varCaracter);
        char varCaracterDecimal = 36; //vaor decimal del juego de caracters unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$'; //un caracter especial,podemos opiar y pegar desde unicode.
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        
        var varCaracter1 = '\u0024';    //indicamos a java la asignacion con el codigo unicode
        System.out.println("varCaracter1 = " + varCaracter1);
        var varCaracterDecimal1 = (char)36; //vaor entero y le asigna un tipo int
        System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
        var varCaracterSimbolo1 = '$'; //un caracter especial,podemos opiar y pegar desde unicode.
        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);
        
        
        int varEnteroChar = '$';
        System.out.println("varEnteroChar = " + varEnteroChar);
        int caracterChar = 'g'; // 103 le corresponde a la letra g en unicode.
        System.out.println("caracterChar = " + caracterChar);
         */
        //clase 6 
        //conversiond e tipos primitivos
//        var edad = Integer.parseInt("20");
//        System.out.println("edad = " + (edad + 1));
//        var valorPi = Double.parseDouble("3.1216");
//        System.out.println("valorPi = " + valorPi);
        //pedir un valor 
//        var entrada = new Scanner(System.in);
//        System.out.println("Digite su edad");
//        edad = Integer.parseInt(entrada.nextLine());
//        System.out.println("edad = " + edad);
        //conversion de tipos primitivos en java Parte 2
//        var edadTexto = String.valueOf(10);
//        System.out.println("edadTexto = " + edadTexto);
//
//        var fraseChar = "programadores".charAt(0);
//        System.out.println("fraseChar = " + fraseChar);
//
//        System.out.println("Digite un caracter: ");
//        fraseChar = entrada.nextLine().charAt(0);
//        System.out.println("fraseChar = " + fraseChar);
//        int num1 = 5, num2 = 4;
//        var solucion = num1 + num2;
//        System.out.println("solucion suma = " + solucion);
//        
//        
//        solucion = num1 - num2;
//        System.out.println(" solucion de la resta = " +  solucion);
//        
//        solucion = num1 * num2;
//        System.out.println(" solucion de la multiplicacion = " +  solucion);
//        
//        solucion = num1 / num2;
//        System.out.println(" solucion de la division = " +  solucion);
//        
//        var solucion2 = 3.4 / num2;
//        System.out.println("solucion2 resultado de la division = " + solucion2);
//        
//        solucion = num1 % num2; //guarda el residuo entero de la division
//        System.out.println("solucion = " + solucion); // 5/4 
//        
//        
//        if (num2 % 2 == 0)
//            System.out.println("ES un numero par");
//        else 
//            System.out.println("Es un numero impar");
//        int varNum1 = 1, varNum2 = 4;
//        int varNum3 = varNum1 + 6 - varNum2; //una operacion
//        System.out.println("varNum3 = "+ varNum3);
//        
//        varNum1 += 1; //narNum1 = varNum + 1;
//        System.out.println("varNum1 = " + varNum1);
        //       -=   *=   /=   %=  
//        varNum1 -= 2;
//        System.out.println("varNum1 = " + varNum1);
//        
//        varNum2 *= 5;
//        System.out.println("varNum2 = " + varNum2);
//        
//        varNum3 /= 3;
//        System.out.println("varNum3 = " + varNum3);
//        
//        varNum2 %= 4;
//        System.out.println("varNum2 = " + varNum2);
//        var varA =7;
//        var varB = -varA;
//        System.out.println("varA = " + varA);
//        System.out.println("varB = " + varB); //el resultado sera un numero regativo.
//        
//        
//        //operador de negacion
//        
//        var varC = true; //esta literal por default en java es de tipo boolean
//        var varD = !varC; //aqui esta invirtiendo el valor.
//        System.out.println("varC = " + varC);
//        System.out.println("varD = " + varD);
//        
//        
//        //operadores unarios de incremento: preincremento
//        
//        var varE =9; //se va a modificar su valor
//        var varF = ++varE; //simbolo antes de la variable
//        
//        //primero se incrementa la v ariable y despues se usa su valor.
//        
//        System.out.println("varE = " + varE); //se incrementa en la unidad
//        System.out.println("varF = " + varF); //va a sumar uno
//        
//        //Postincremento (el simbolo va despues de la variable)
//        
//        var varG = 3;
//        var varH = varG++;
//        System.out.println("varG = " + varG);
//        System.out.println("varH = " + varH);
//        
//        
//       // operadores unarios de  decremento: predecremento
//       
//       var varI =4;
//       var varJ = --varI;
//        System.out.println("varI = " + varI); //la variable ya esta con decremento
//        System.out.println("varJ = " + varJ);
//        
//        //postdecremento
//        
//        var varK = 8;
//        var varL = varK--; //primero el valor de la variable, luego queda el decremento
//        System.out.println("varK = " + varK);//aqui va a decrementar el 1
//        System.out.println("varL = " + varL);
        //operadores de igualdad y relacionales
//        var aNum = 5;
//        var bNum = 4;
//        var cNum = (aNum == bNum);
//        System.out.println("cNum = " + cNum);
//        
//        var dNum = aNum != bNum;
//        System.out.println("dNum = " + dNum);
//        
//        var cadenaA = "hello";
//        var cadenaB = "bye bye";
//        var cVar = cadenaA == cadenaB;
//        System.out.println("cVar = " + cVar);
//        
//        var fVar = cadenaA.equals(cadenaB);
//        System.out.println("fVar = " + fVar);
//        
//        var gVar = aNum >= bNum; //  > >= < <= == !=
//        System.out.println("gVar = " + gVar);
//        
//        if (aNum % 2 == 0)
//            System.out.println("El numero es par");
//     else 
//            System.out.println("El numero es impar");
//   
//        var edad = 30;
//        var adulto =18;
//        if (edad >= adulto) {
//            System.out.println("Es mayor de edad");
//        }
//        else {
//            System.out.println("Es menor de edad");
//        }
        /*var valorA = 7;
        var valorMinimo = 0;
        var valorMaximo = 10;
        var respuesta = valorA >= 0 && valorA <= 10;

        if (respuesta) {
            System.out.println("esta dentro del rango establecido");
        } else {
            System.out.println("esta fuera del rango establecido");
        }

        var vacaciones = false;
        var diaLibre = true;
        if (vacaciones || diaLibre) {
            System.out.println("Papa puede asistir al juego de su hijo");
        } else {
            System.out.println("papa no puede asistir al juegod e su hijo");
        }
        */
        
        //OPERADOR TERNARIO
        
        /*var resultadoT = (5 > 8) ? "verdadero" : "falso";
        System.out.println("resultadoT = " + resultadoT);
        
        var numeroT = 4;
        resultadoT = (numeroT % 2 == 0) ? "es par" : "es impar";
        System.out.println("resultadoT = " + resultadoT);
        */
        
        var x = 5;
        var y = 10;
        var z = ++x + y--;
        
        System.out.println("x = " + x); //6
        System.out.println("y = " + y);// 9
        System.out.println("z = " + z);// 16
        
        var solucionAritmetica = 4 + 5 * 6 / 3; // 4 + ((5*6) / 3) = 30 / 3 = 10 + 4 =14 
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        
        solucionAritmetica = (4 + 5) * 6 / 3; // 4+5 = 9 * 6 = 54 / 3 = 18
        
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        
       
        
        
        
    }
}
