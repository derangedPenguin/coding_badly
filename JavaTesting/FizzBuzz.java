import java.util.Scanner;

public class FizzBuzz {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String output = "";
        String[] strings = {"Pop","Fizz","Buzz","Bang","Pow"};
        int[] factors = {7,5,3,2,11};

        while (true) {
            output = "";
            System.out.print("Num: ");
            long num = scanner.nextLong();

            if (num == 123456789)
                break;

            for (int i = 0; i < strings.length; i++){
                if (num % factors[i] == 0)
                    output += strings[i];
            }
            if (output.isBlank()) {
                output += num;
            }
            System.out.println(output);
        }
        scanner.close();
    }
}
