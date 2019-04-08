/*Mohammed Alshuyukh
 * ID: 991349088
 * 
 * 
 */

import java.util.Scanner;

public class Lab07_V2 {
	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		int n = stdIn.nextInt(); //Variable for validation loop

		//User Validation loop
		while(n>9 || n<1) 
		{
			if (n >= 1 || n <=9) 
			{
				System.out.print(n);
			}
			
			else 
			{
				System.out.println("Do it again");
			}
		}

		//For loop
		for(int i = 1; i<=n; i++) //When I is less then or equal to the input 
		{	
			//Printing spaces starting from the left
			for(int j = n-i; j>0;j--)  
			{
				System.out.print(" "); 
			}

			//Printing our numbers starting from highest until it reaches 1
			for(int k = i; k>0; k--) 
			{
				System.out.print(k);
			}
			for(int v = 0; v<i; v++) //initialized at 0 because when I did 1, it didn't print the other 1, so I added 0 then added 1 manually .
			{
				System.out.print(v + 1);
			}
			System.out.println();
		}


		stdIn.close();
	}

}
