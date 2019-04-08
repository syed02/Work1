
public class Q5 {
	public static void main(String [] args) 
	{
		int loopNum = 1;
		int sum = 0;

		do 
		{

			if (loopNum %2 != 0) 
			{
				sum += loopNum;
				loopNum += 2;
			}

		}while (loopNum >= 1 && loopNum <= 21);
		System.out.println("sum is equal to: " + sum);

	}
}
