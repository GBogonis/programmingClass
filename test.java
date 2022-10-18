import java.util.Scanner;  // Import the Scanner class


public class test {

    public static void main(String[] args) {
        System.out.println("hello wolrd");
        Scanner myObj = new Scanner(System.in);  // Create a Scanner object
        System.out.println("Enter number");
        int num = myObj.nextInt();  // Read user input
        System.out.println(10 + num);  // Output user input
    }

}