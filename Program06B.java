import java.util.Scanner;

public class Program06B {
	public static void main (String[] args) 
	{
		Scanner stdIn = new Scanner(System.in);
		String yesno;
		int choice;
		int wins = 0;
		int loss = 0;
		int rounds = 0;
		int choose;
		/*
	System.out.println("Welcome to Computer Dice");
	System.out.println("-------------------------------------\n");
	System.out.println("You will first roll your dice\r\n" + 
			"You then are allowed to re-roll upto\r\n" + 
			"two of your dice\r\n" + 
			"Finally the outcome of your roll is\r\n" + 
			"be determined:\r\n" + 
			"any Quad and you receive 108 Wins\r\n" + 
			"any Triple and you receive 6 wins\r\n" + 
			"any Two-Pair and you receive 4 Wins\r\n" + 
			"anything else and you receive 1 Lose");
		 */

		System.out.println("Player\r\n" + 
				"----------");

		do {

			int d1 = (int)(Math.random() * 6) + 1;
			int d2 = (int)(Math.random() * 6) + 1;
			int d3 = (int)(Math.random() * 6) + 1;
			int d4 = (int)(Math.random() * 6) + 1;
			System.out.println(d1 + "  " + d2 + "  " + d3 + "  " + d4);



			do 
			{
				System.out.println("Pick how many dies to reroll");
				choice = stdIn.nextInt();
			}while(choice < 0 && choice > 2); 

			{
				if (choice == 0) 
				{

				}

				else if (choice == 1) 
				{
					System.out.println("Please enter the number of die to reroll: ");					
					choose = stdIn.nextInt();
					if (choose == 1) 
					{
						d1 = (int)(Math.random() * 6) + 1;
					}

					else if (choose == 2) 
					{
						d2 = (int)(Math.random() * 6) + 1;
					}
					else if (choose == 3) 
					{
						d3 = (int)(Math.random() * 6) + 1;
					}
					else if (choose == 4)
					{
						d4 = (int)(Math.random() * 6) + 1;
					}

				}
				else if (choice == 2) 
				{
					System.out.println("Please enter the number of die to reroll: ");					
					choose = stdIn.nextInt();
					if (choose == 1) 
					{
						d1 = (int)(Math.random() * 6) + 1;
					}

					else if (choose == 2) 
					{
						d2 = (int)(Math.random() * 6) + 1;
					}
					else if (choose == 3) 
					{
						d3 = (int)(Math.random() * 6) + 1;
					}
					else if (choose == 4)
					{
						d4 = (int)(Math.random() * 6) + 1;
					}

					System.out.println("Please enter the number of die to reroll: ");					
					choose = stdIn.nextInt();
					if (choose == 1) 
					{
						d1 = (int)(Math.random() * 6) + 1;
					}

					else if (choose == 2) 
					{
						d2 = (int)(Math.random() * 6) + 1;
					}
					else if (choose == 3) 
					{
						d3 = (int)(Math.random() * 6) + 1;
					}
					else if (choose == 4)
					{
						d4 = (int)(Math.random() * 6) + 1;
					}


				}

			}
			System.out.println("Player\r\n" + 
					"----------");
			System.out.println(d1 + "  " + d2 + "  " + d3 + "  " + d4);


			if (d1 == d2 && d1 == d3 && d1 == d4) 
			{
				wins += 108;
				System.out.println("Quad - Congrats, you win!");
			}
			else if ((d1 == d2 && d1 == d3) || (d1 == d2 && d1 == d4) || (d1 == d3 && d1 == d4) ) 
			{
				wins += 6;
				System.out.println("Triple - Congrats, you win!");
			}

			else if ((d2 == d1 && d2 == d3) || (d2 == d3 && d2 == d4) || (d2 == d1 && d2 == d4)) 
			{
				wins += 6;
				System.out.println("Triple - Congrats, you win!");
			}

			else if ((d3 == d1 && d3 == d4) || (d3 == d1 && d3 == d2) || (d3 == d2 && d3 == d4)) 
			{
				wins += 6;
				System.out.println("Triple - Congrats, you win!");
			}

			else if ((d4 == d1 && d4 == d2) || (d4 == d1 && d4 == d3) || (d4 == d2 && d4 == d3)) 
			{
				wins += 6;
				System.out.println("Triple - Congrats, you win!");
			}

			else if ((d1 == d2) || (d1 == d3)  || (d1 == d4)) 
			{
				wins += 4;
				System.out.println("Twin - Congrats, you win!");
			}

			else if ((d2 == d1) || (d2 == d3) || (d2 == d4)) 
			{
				wins += 4;
				System.out.println("Twin - Congrats, you win!");
			}

			else if ((d3 == d1) || (d3 == d2) || (d3 == d4)) 
			{
				wins += 4;
				System.out.println("Twin - Congrats, you win!");
			}

			else if ((d4 == d1) || (d4 == d2) || (d4 == d3)) 
			{
				wins += 4;
				System.out.println("Twin - Congrats, you win!");
			}

			else
			{
				System.out.println("Junker, sorry, you lose");
				loss += 1;

			}

			System.out.println("Do you wish to play again [y,n]: ");
			yesno = stdIn.next();
			rounds++;

		}while (!yesno.equals("n") || yesno.equals("y"));

		System.out.println("Thank you for playing");
		System.out.println("You played " + rounds + " rounds");
		System.out.println("wins: " + wins);
		System.out.println("losses: " + loss);
		stdIn.close();
	}
}
