import java.util.Scanner;  // Import the Scanner class


public class test {

    public static void main(String[] args) {
        System.out.println("hello wolrd");
        try (Scanner Scanner = new Scanner(System.in)) {
            System.out.println("Enter number");
            int num = Scanner.nextInt();  // Read user input
            System.out.println(10 + num);  // Output user input
        }
    }

}