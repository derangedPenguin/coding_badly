import java.text.NumberFormat;
import java.util.Scanner;

public class MortgageCalc{
    public static void main(String[] args){
        final byte PERCENT = 100;
        final byte MONTHS = 12;
        
        int principal = 0;
        float monthlyRate = 0;
        int totalPayments = 0;

        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("Principal ($1k-$1m): ");
            principal = scanner.nextInt();
            if (principal <= 1_000_000 && principal >= 1000) {
                break;
            }
            System.out.println("Please enter a value between 1000 & 1000000");
        }
        while (true) {
            System.out.print("Annual Interest Rate: ");
            float annualRate = scanner.nextFloat();
            if (annualRate <= 30 && annualRate > 0) {
                monthlyRate = annualRate / PERCENT / MONTHS;
                break;
            }
            System.out.println("Please enter a value greater than 0 & up to 30");
        }
        while (true) {
            System.out.print("Period (Years): ");
            int years = scanner.nextInt();
            if (years <= 30 && years >= 1) {
                totalPayments = years * MONTHS;
                break;
            }
            System.out.println("Please enter a value between 1 & 30");
        }

        double mortgage = principal
                            *(monthlyRate*Math.pow((1+monthlyRate),totalPayments)
                            /(Math.pow((1+monthlyRate),totalPayments)-1));
        String mortgageFormated = NumberFormat.getCurrencyInstance().format(mortgage);

        System.out.println("Mortgage: "+mortgageFormated);

        scanner.close();
    }
}