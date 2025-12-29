// Program to reverse a given number
public class ReverseNumber {

    public static void main(String[] args) {

        // Original number
        int number = 12345;

        // Variable to store reversed number
        int reversed = 0;

        // Loop until the number becomes 0
        while (number != 0) {
            int digit = number % 10;   // Get last digit
            reversed = reversed * 10 + digit; // Build reversed number
            number = number / 10;      // Remove last digit
        }

        // Print the reversed number
        System.out.println("Reversed number: " + reversed);
    }
}
