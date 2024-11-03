import java.util.Random;
import java.util.Scanner;

public class DiceRollingSimulator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        String rollAgain;

        do {
            // Generate a random number between 1 and 6 for dice roll
            int diceRoll = random.nextInt(6) + 1;
            System.out.println("You rolled a " + diceRoll + ".");

            // Ask the user if they want to roll the dice again
            System.out.println("Do you want to roll again? (yes/no)");
            rollAgain = scanner.nextLine();

        } while (rollAgain.equalsIgnoreCase("yes"));

        System.out.println("Thank you for playing!");
        scanner.close();
    }
}
