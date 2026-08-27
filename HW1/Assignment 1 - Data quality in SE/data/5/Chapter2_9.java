import java.util.Scanner;

public class Chapter2_9 {
    public static void main(String[] args) {
        System.out.println("Please enter the number: ");
        Scanner input = new Scanner(System.in);
        int amount = input.nextInt();
        int numOfOneDollars = amount / 100;
        amount = amount % 100;

        // Find the number of quarters in the remaining amount
        int numOfQuarters = amount / 25;
        amount = amount % 25;

        // Find the number of dimes in the remaining amount
        int numOfDimes = amount / 10;
        amount = amount % 10;

        // Find the number of nickels in the remaining amount
        int numOfNickels = amount / 5;
        amount = amount % 5;

        // Find the number of pennies in the remaining amount
        int numOfPennies = amount;

        // Display results
        System.out.println("Your amount " + amount + " consists of ");
        System.out.println(numOfOneDollars + "\t dollars");
        System.out.println(numOfQuarters + "\t quarters");
        System.out.println(numOfDimes + "\t dimes");
        System.out.println(numOfNickels + "\t nickels");
        System.out.println(numOfPennies + "\t pennies");

    }
}
