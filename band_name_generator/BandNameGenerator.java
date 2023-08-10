package band_name_generator;
import java.util.*;


public class BandNameGenerator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the city you grew up in: ");
        String city = sc.nextLine();
        System.out.println("Enter the name of a pet you know: ");
        String pet_name = sc.nextLine();

        System.out.println("Your band name could be " + city + " " + pet_name);
    }
}