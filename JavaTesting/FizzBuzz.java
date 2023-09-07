import java.util.HashMap;
import java.util.Scanner;

public class FizzBuzz {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String output = "";
        HashMap<Integer, String> pairs = new HashMap<Integer, String>();
        pairs.put(2,"Pow");
        pairs.put(3,"Fizz");
        pairs.put(5,"Buzz");
        pairs.put(7,"Pop");
        pairs.put(11,"Bang");
        
        while (true) {
            output = "";
            System.out.print("Num: ");
            long num = scanner.nextLong();

            if (num == 123456789)
                break;

            for (int factor : pairs.keySet()){
                if (num % factor == 0)
                    output += pairs.get(factor);
            }
            if (output.isBlank()) {
                output += num;
            }
            System.out.println(output);
        }
        scanner.close();
    }
}
