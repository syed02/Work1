import java.util.Scanner;

public class Examples {
	public static void main(String[] args) {

		Scanner stdIn = new Scanner(System.in);
		double int1;
		double int2;

		System.out.print("Enter int1 number: ");
		int1 = stdIn.nextDouble();
		System.out.println("Enter int2 number: ");
		int2 = stdIn.nextDouble();

		String yoda = "May the force be with you.";
		System.out.println(yoda.substring(8));
		System.out.println(yoda.substring(4, 13));


		String egyptian = "I will not leave the square. Over my dead body.";
		int index = egyptian.indexOf('n');
		String egyptian2 = egyptian.substring(index );
		System.out.println(egyptian2); 


		double pow = Math.pow(int1, int2);
		System.out.println("The number raised to the specific power is: " + pow );

		double minimum = Math.min(int1, int2);
		System.out.println("The less positve of the two double values of int1, int2 is: " + minimum);

		double pi = Math.PI;
		System.out.println("Pi is: " + pi);
	}

}
