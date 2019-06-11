package Bunk;
import java.util.*;
public class PayOutofBounds extends Exception
{
	public PayOutofBounds(String s)
	{
		super(s);
	}
	
	public float See(float x,float y)
	{
		
		
	
		try
		{
			
			if(x<0)
			{
				PayOutofBounds k=new PayOutofBounds("Attended lecs cannot be negative");
				throw k;
				
			}
			
		}
		
		catch(PayOutofBounds a)
		{
			System.out.println("Attended  lecs cannot be negative"+a);
			return(-1f);
		}
		try
		{
				
			if(x<y)
			{
				PayOutofBounds sal=new PayOutofBounds("Bunked lectures cannot be greater than attended");
				throw sal;
			}
		}
		catch(PayOutofBounds sal)
		{
			System.out.println("Bunked lectures cannot be greater than attended"+sal);
			return(101f);
		}
		if(y==0)
			return(100f);
		else
		return((y/x)*100f);
	}
}
