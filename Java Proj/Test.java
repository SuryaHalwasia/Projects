import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import Bunk.*;

public class Test //extends Frame  implements ActionListener
{
	Test()
	{
				JFrame frame5 = new JFrame("Bunk Calci");
       frame5.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		JPanel comps1 = (JPanel)frame5.getContentPane();
		JLabel c11 = new JLabel();
		c11.setIcon(new ImageIcon("math.jpg"));
        comps1.add(c11);
		JLabel l1=new JLabel("Total lecs");
		l1.setBounds(300,0,500,500);
		l1.setFont(l1.getFont().deriveFont(23f));
		c11.add(l1);
		JTextField j1=new JTextField(10);
		j1.setBounds(800,225,100,30);
		j1.setFont(j1.getFont().deriveFont(23f));
		c11.add(j1);


		JTextField j2=new JTextField(10);
		j2.setBounds(800,275,100,30);
		j2.setFont(j1.getFont().deriveFont(23f));
		c11.add(j2);

		JLabel l2=new JLabel("Bunked Lecs");
		l2.setBounds(300,50,500,500);
		l2.setFont(l1.getFont().deriveFont(23f));
		c11.add(l2);
		JButton b1=new JButton("SUBMIT");
		b1.setBounds(550, 500, 100, 40);
		c11.add(b1);
		
		
		
				b1.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				String s1,s2;
				s1=j1.getText();
				s2=j2.getText();
				float a=Float.parseFloat(s1);
				float b=Float.parseFloat(s2);
				j2.setText(s1);
				System.out.println(a+b);
				
				String s=new String("s");
				PayOutofBounds c=new PayOutofBounds(s);
				float ef=c.See(a,b);
				double d=Math.round((ef*100.0)/100.0);
				
				j1.setText(String.valueOf(d));
				
			}  
		}
		);
		frame5.setLocationRelativeTo(null);
        frame5.pack();
        frame5.setVisible(true);
	}
	public static void main(String[] args)
	{
		Test t=new Test();
	}}