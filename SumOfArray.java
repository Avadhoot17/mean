// Program to calculate the sum of elements in an array
public class SumOfArray {

    public static void main(String[] args) {

        // Initialize an integer array
        int[] arr = {2, 4, 6, 8, 10};

        // Variable to store the sum
        int sum = 0;

        // Loop through the array and add each element
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
        }

        // Print the final sum
        System.out.println("Sum of elements: " + sum);
    }
}
