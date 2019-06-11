import javax.swing.*;
import java.awt.*;
class Demo extends JFrame
{
	JLabel name=new JLabel();
	JLabel username=new JLabel();
	JLabel password=new JLabel();
	JLabel ren=new JLabel();
	Demo()
	{
		JLabel background;                                                                                   
		setTitle("MAP");
		setSize(1200,700);
		setLayout(null);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		ImageIcon img=new ImageIcon("images2.jpg");
		background=new JLabel("",img, JLabel.CENTER);
		
	setVisible(true);
	}
}

class B
{
	public static void main(String[] args)
	{
		Demo d1=new Demo();
	}
}