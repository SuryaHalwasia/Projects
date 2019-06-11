import java.util.*;
class BunkException extends Exception
{
	BunkException(String s)
	{
		super(s);
	}
}
class TestBunk1 
{
	public static void main(String args[])throws IOException
	{
		int x,y;
		Scanner sc=new Scanner(System.in);
		x=sc.nextInt();
		y=sc.nextInt();
		try
		{
			if(x<0)
			{
				BunkException b=new BunkException("Less than 0");
				throw b;
			}
		}
		catch(BunkException b)
		{
			 System.out.println("Lecs cant be less than 0");
		}
	}
}
