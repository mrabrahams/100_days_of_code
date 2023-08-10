import java.util.*;

public class TipCalculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        int patrons = 0;
        int tip = 0;
        int total = 0;
        int tip_percent = 0;
        int total_bill = 0;

        System.out.println("Welcome to the tip calculator.\n Enter the number of patrons: ");
        patrons = input.nextInt();
        System.out.println("Enter the total bill: ");
        total = input.nextInt();
        System.out.println("Enter the tip percentage: ");
        tip_percent= input.nextInt();
        System.out.println("You entered " + patrons + " patrons, a total bill of $" + total + ", and a tip percentage of " + tip_percent + "%.");
        tip = (tip_percent * total) / 100;
        System.out.println("The tip is: $" + tip);

        total_bill = total +  tip;
        System.out.println("The total bill is: $" + total_bill);
        
        System.out.println("Each person will have to pay: $" + total_bill/patrons);

        input.close();
    }
}
