import java.util.*;
class BunkException extends Exception
{
  BunkException(String s)
  {
    super(s);
	}
	}
	class TestBunk
	{
	   int Bunk(int a, int b1)
	   {
	      int lecs=a,bunk=b1;
		  try
		  {
		   
		   if(a<0)
		   {
			  BunkException b=new BunkException("Less than 0");
		      throw b;
			  }
			  }
			  catch(BunkException b)
			  {
			  System.out.println("Lecs cant be less than 0");
			  return(-1);
			  }
			 try
			 {
				 if(a<b1)
				 {
					 BunkException b=new BunkException("Bunk lecs more than total");
					 throw b;
				 }
			 }
			 catch(BunkException b)
			 {
				 System.out.println("Bunked Lecs cant be greater than attended lecs");
				 return(101);
			 }
	   
	  
	   return(a+b1);
	   }
	public static void main(String args[]) 
	{
		int a,b1;
		Scanner sc=new Scanner(System.in);
		a=sc.nextInt();
		b1=sc.nextInt();
		TestBunk t=new TestBunk();
		int n=t.Bunk(a,b1);
		System.out.println(n);
	}
	}
	

	

			  
			  
			  