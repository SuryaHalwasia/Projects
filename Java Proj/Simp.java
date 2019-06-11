import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import Bunk.*;
class D{
	D() {
        JFrame frame = new JFrame("LOGIN");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		JPanel panel = (JPanel)frame.getContentPane();
		JLabel label = new JLabel();
      
		 label.setIcon(new ImageIcon("images2.jpg"));
        panel.add(label);
		JLabel l1=new JLabel("Name");
		l1.setBounds(300,0,500,500);
		l1.setFont(l1.getFont().deriveFont(23f));
		label.add(l1);
		

		JLabel l2=new JLabel("Username");
		l2.setBounds(300,50,500,500);
		l2.setFont(l1.getFont().deriveFont(23f));
		label.add(l2);

		JLabel l3=new JLabel("Password");
		l3.setBounds(300,100,500,500);
		l3.setFont(l3.getFont().deriveFont(23f));
		label.add(l3);

		JLabel l4=new JLabel("Re-Enter");
		l4.setBounds(300,150,500,500);
		l4.setFont(l1.getFont().deriveFont(23f));
		label.add(l4);

		
		JTextField j1=new JTextField(10);
		j1.setBounds(800,225,100,30);
		j1.setFont(j1.getFont().deriveFont(23f));
		label.add(j1);


		JTextField j2=new JTextField(10);
		j2.setBounds(800,275,100,30);
		j2.setFont(j1.getFont().deriveFont(23f));
		label.add(j2);

		JTextField j3=new JTextField(10);
		j3.setBounds(800,325,100,30);
		j3.setFont(j1.getFont().deriveFont(23f));
		label.add(j3);

		JTextField j4=new JTextField(10);
		j4.setBounds(800,375,100,30);
		j4.setFont(j1.getFont().deriveFont(23f));
		label.add(j4);

 
		JButton b1=new JButton("SUBMIT");
		b1.setBounds(550, 500, 100, 40);
		label.add(b1);
		b1.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				if((j1.getText().equals(""))&&(j2.getText().equals(""))&&(j3.getText().equals(""))&&(j4.getText().equals("")))
				{
							System.out.println("Enter");
				}
				else
				{Fra me=new Fra();
				frame.setVisible(false);}
			}  
		}
		);  
		
		

		frame.setLocationRelativeTo(null);
		frame.setBounds(0,0,1000,1000);
        frame.pack();
		
        frame.setVisible(true);
    }
}
	/*public void actionPerformed(ActionEvent ae)
	{
		if(ae.getActionCommand().equals("SUBMIT"))
		{
			frame.setVisible(false);
		}

	}
}
*/

class Simp
{
    public static void main (String args[]) 
	{
		D d=new D();
		
		

	}
}


class Fra 
{
	Fra()
	{
		JFrame frame2 = new JFrame("CHOOSE STREAM");
        frame2.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		JPanel panel1 = (JPanel)frame2.getContentPane();
		JLabel labela = new JLabel();
		labela.setIcon(new ImageIcon("images1.jpg"));
        panel1.add(labela);
	

		JLabel m1=new JLabel("BIOMED");
		m1.setBounds(10,0,500,300);
		m1.setFont(m1.getFont().deriveFont(23f));
		labela.add(m1);
		
		JLabel m2=new JLabel("EXTC");
		m2.setBounds(1250,0,500,300);
		m2.setFont(m1.getFont().deriveFont(23f));
		labela.add(m2);
		JLabel m3=new JLabel("IT");
		m3.setBounds(10,500,500,300);
		m3.setFont(m1.getFont().deriveFont(23f));
		labela.add(m3);
		JLabel m4=new JLabel("CHEMICAL");
		m4.setBounds(1250,500,500,300);
		m4.setFont(m1.getFont().deriveFont(23f));
		labela.add(m4);
		JLabel m5=new JLabel("COMPS");
		m5.setBounds(650,250,500,300);
		m5.setFont(m1.getFont().deriveFont(23f));
		labela.add(m5);
		JButton b14=new JButton(); //Comps
		b14.setBounds(700,350, 10, 10);
		labela.add(b14);
				b14.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				Comps me=new Comps();
				me.Choose();
				frame2.setVisible(false);
			}  
		}
		);  
		JButton b10=new JButton();//Biomed
		b10.setBounds(30, 100, 10, 10);
		labela.add(b10);
		b10.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				Bio me=new Bio();
				me.Stream();
				frame2.setVisible(false);
			}  
		}
		);  
		JButton b11=new JButton();//EXTC
		b11.setBounds(1270, 100, 10, 10);
		labela.add(b11);
		b11.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				Extc me=new Extc();
				me.Stream();
				frame2.setVisible(false);
			}  
		}
		);
		JButton b12=new JButton();//iT
		b12.setBounds(20,600, 10, 10);
		labela.add(b12);
						b12.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				It me=new It();
				me.Choose();
				frame2.setVisible(false);
			}  
		}
		); 
		JButton b13=new JButton();//chemical
		b13.setBounds(1300,600, 10, 10);
		labela.add(b13);
		b13.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				Chem me=new Chem();
				me.Stream();
				frame2.setVisible(false);
			}  
		}
		);  
		
		
		
		
		
		frame2.setLocationRelativeTo(null);
        frame2.pack();
		frame2.setBounds(0,0,1500,1000);
        frame2.setVisible(true);
		
	}
}


abstract class Branch
{
//	abstract void Stream();
}

class Branches extends Branch
{
	void Choose()
	{
		System.out.println("This does nothing");
	}
}

class Extc extends Branch
{
	public void Stream()
	{
		JFrame frame3 = new JFrame("EXTC");
        frame3.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		JPanel panelb = (JPanel)frame3.getContentPane();
		JLabel labele1 = new JLabel();
		labele1.setIcon(new ImageIcon("extc.jpg"));
        panelb.add(labele1);
		JButton b13=new JButton();//bunk
		b13.setBounds(100,400, 10, 10);
		b13.setBackground(Color.cyan);
			JLabel lo1=new JLabel("BUNK CALCI");
		lo1.setBounds(30,220,500,300);
		lo1.setFont(lo1.getFont().deriveFont(23f));
		labele1.add(lo1);
		labele1.add(b13);
		JButton b14=new JButton();//bunk
		b14.setBounds(800,400, 10, 10);
		b14.setBackground(Color.cyan);
			JLabel lo2=new JLabel("TIMETABLE");
		lo2.setBounds(730,220,500,300);
		lo2.setFont(lo1.getFont().deriveFont(23f));
		labele1.add(lo2);
		labele1.add(b14);
		JLabel lo=new JLabel("ROOM=702 NB");
		lo.setBounds(150,0,500,300);
		lo.setFont(lo.getFont().deriveFont(23f));
		labele1.add(lo);
				b13.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				Bunkie me=new Bunkie();
			
				frame3.setVisible(false);
			}  
		}
		);  
				b14.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				TEx me=new TEx();
				me.Fill();
				frame3.setVisible(false);
			}  
		}
		);  
		
		frame3.setLocationRelativeTo(null);
        frame3.pack();
		frame3.setBounds(0,0,1500,1000);
        frame3.setVisible(true);
		
	}
}

class Comps extends Branches
{
		void Choose()
		{
			JFrame frame4 = new JFrame("CHOOSE");
			frame4.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			JPanel panelc = (JPanel)frame4.getContentPane();
			JLabel labelco = new JLabel();
			labelco.setIcon(new ImageIcon("comps.jpg"));
			panelc.add(labelco);
			JButton c1=new JButton("C1");
			c1.setBounds(100,400, 200, 50);
			c1.setBackground(Color.yellow);
			labelco.add(c1);
					c1.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				Comps1 me=new Comps1();
				me.Stream();
				frame4.setVisible(false);
			}  
		}
		);  
			JButton c2=new JButton("C2");
			c2.setBounds(950,400, 200, 50);
			c2.setBackground(Color.yellow);
			labelco.add(c2);
								c2.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				Comps2 me=new Comps2();
				me.Stream();
				frame4.setVisible(false);
			}  
		}
		);  
			frame4.setLocationRelativeTo(null);
			frame4.pack();
			frame4.setBounds(0,0,1500,1000);
			frame4.setVisible(true);
		}
}

class Comps1 extends Branches
{
		public void Stream()
	{
		JFrame frame5 = new JFrame("C1");
        frame5.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		JPanel comps1 = (JPanel)frame5.getContentPane();
		JLabel c11 = new JLabel();
		c11.setIcon(new ImageIcon("c1.jpg"));
        comps1.add(c11);
		
		JLabel co=new JLabel("ROOM=505 NB");
		co.setBounds(200,0,500,300);
		co.setFont(co.getFont().deriveFont(23f));
		co.setBackground(Color.white);
		co.setForeground(Color.black);
		c11.add(co);
		JButton b14=new JButton();//bunk
		b14.setBounds(800,400, 10, 10);
		b14.setBackground(Color.cyan);
			JLabel lo2=new JLabel("TIMETABLE");
		lo2.setBounds(730,220,500,300);
		lo2.setForeground(Color.black);
		lo2.setFont(lo2.getFont().deriveFont(23f));
		c11.add(lo2);
		c11.add(b14);
		JButton b13=new JButton();//bunk
		b13.setBounds(100,400, 10, 10);
		b13.setBackground(Color.cyan);
		JLabel lo1=new JLabel("BUNK CALCI");
		lo1.setBounds(30,220,500,300);
		lo1.setFont(lo1.getFont().deriveFont(23f));
		lo1.setForeground(Color.black);
		c11.add(lo1);
		c11.add(b13);
				b13.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				Bunkie me=new Bunkie();
			
				frame5.setVisible(false);
			}  
		}
		);  
						b14.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				TCo1 me=new TCo1();
				me.Fill();
				frame5.setVisible(false);
			}  
		}
		);  
		
		frame5.setLocationRelativeTo(null);
        frame5.pack();
		frame5.setBounds(0,0,1500,1000);
        frame5.setVisible(true);
		
	}
}

class Comps2 extends Branches
{
		public void Stream()
	{
		JFrame frame5 = new JFrame("C2");
        frame5.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		JPanel comps1 = (JPanel)frame5.getContentPane();
		JLabel c11 = new JLabel();
		c11.setIcon(new ImageIcon("c1.jpg"));
        comps1.add(c11);
		
		JLabel co=new JLabel("ROOM=508 NB");
		co.setBounds(150,0,500,300);
		co.setFont(co.getFont().deriveFont(23f));
		co.setBackground(Color.white);
		co.setForeground(Color.black);
		c11.add(co);
				JButton b14=new JButton();//bunk
		b14.setBounds(800,400, 10, 10);
		b14.setBackground(Color.cyan);
			JLabel lo2=new JLabel("TIMETABLE");
		lo2.setBounds(730,220,500,300);
		lo2.setForeground(Color.black);
		lo2.setFont(lo2.getFont().deriveFont(23f));
		c11.add(lo2);
		c11.add(b14);
		JButton b13=new JButton();//bunk
		b13.setBounds(100,400, 10, 10);
		b13.setBackground(Color.cyan);
		JLabel lo1=new JLabel("BUNK CALCI");
		lo1.setBounds(30,220,500,300);
		lo1.setFont(lo1.getFont().deriveFont(23f));
		lo1.setForeground(Color.black);
		c11.add(lo1);
		c11.add(b13);
				b13.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				Bunkie me=new Bunkie();
			
				frame5.setVisible(false);
			}  
		}
		);  
								b14.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				TCo2 me=new TCo2();
				me.Fill();
				frame5.setVisible(false);
			}  
		}
		);  
		
		
		frame5.setLocationRelativeTo(null);
        frame5.pack();
		frame5.setBounds(0,0,1500,1000);
        frame5.setVisible(true);
		
	}
}

class It extends Branches
{
		void Choose()
		{
			JFrame frame4 = new JFrame("CHOOSE");
			frame4.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			JPanel panelc = (JPanel)frame4.getContentPane();
			JLabel labelco = new JLabel();
			labelco.setIcon(new ImageIcon("it.jpg"));
			panelc.add(labelco);
			JButton s1=new JButton("S1");
			s1.setBounds(100,400, 200, 50);
			s1.setBackground(Color.yellow);
			labelco.add(s1);
								s1.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				It1 me=new It1();
				me.Stream();
				frame4.setVisible(false);
			}  
		}
		);  
			JButton s2=new JButton("S2");
			s2.setBounds(950,400, 200, 50);
			s2.setBackground(Color.yellow);
			labelco.add(s2);
								s2.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				It2 me=new It2();
				me.Stream();
				frame4.setVisible(false);
			}  
		}
		);  
			frame4.setLocationRelativeTo(null);
			frame4.pack();
			frame4.setBounds(0,0,1500,1000);
			frame4.setVisible(true);
		}
}

class It1 extends Branches
{
		public void Stream()
	{
		JFrame frame5 = new JFrame("S1");
        frame5.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		JPanel comps1 = (JPanel)frame5.getContentPane();
		JLabel c11 = new JLabel();
		c11.setIcon(new ImageIcon("it.jpg"));
        comps1.add(c11);
		
		JLabel co=new JLabel("ROOM=801 NB");
		co.setBounds(200,0,500,300);
		co.setFont(co.getFont().deriveFont(23f));
		co.setBackground(Color.white);
		co.setForeground(Color.black);
		c11.add(co);
		JButton b14=new JButton();//bunk
		b14.setBounds(800,400, 10, 10);
		b14.setBackground(Color.cyan);
			JLabel lo2=new JLabel("TIMETABLE");
		lo2.setBounds(730,220,500,300);
		lo2.setForeground(Color.black);
		lo2.setFont(lo2.getFont().deriveFont(23f));
		c11.add(lo2);
		c11.add(b14);
		JButton b13=new JButton();//bunk
		b13.setBounds(100,400, 10, 10);
		b13.setBackground(Color.cyan);
		JLabel lo1=new JLabel("BUNK CALCI");
		lo1.setBounds(30,220,500,300);
		lo1.setFont(lo1.getFont().deriveFont(23f));
		lo1.setForeground(Color.black);
		c11.add(lo1);
		c11.add(b13);
				b13.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				Bunkie me=new Bunkie();
			
				frame5.setVisible(false);
			}  
		}
		);  
									b14.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				TIt1 me=new TIt1();
				me.Fill();
				frame5.setVisible(false);
			}  
		}
		);  
		
		
		
		frame5.setLocationRelativeTo(null);
		frame5.setBounds(0,0,1500,1000);
        frame5.pack();
        frame5.setVisible(true);
		
	}
}

class It2 extends Branches
{
		public void Stream()
	{
		JFrame frame5 = new JFrame("S2");
        frame5.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		JPanel comps1 = (JPanel)frame5.getContentPane();
		JLabel c11 = new JLabel();
		c11.setIcon(new ImageIcon("it.jpg"));
        comps1.add(c11);
		
		JLabel co=new JLabel("ROOM=802 NB");
		co.setBounds(150,0,500,300);
		co.setFont(co.getFont().deriveFont(23f));
		co.setBackground(Color.white);
		co.setForeground(Color.black);
		c11.add(co);
		JButton b14=new JButton();//bunk
		b14.setBounds(800,400, 10, 10);
		b14.setBackground(Color.cyan);
			JLabel lo2=new JLabel("TIMETABLE");
		lo2.setBounds(730,220,500,300);
		lo2.setForeground(Color.black);
		lo2.setFont(lo2.getFont().deriveFont(23f));
		c11.add(lo2);
		c11.add(b14);
		JButton b13=new JButton();//bunk
		b13.setBounds(100,400, 10, 10);
		b13.setBackground(Color.cyan);
		JLabel lo1=new JLabel("BUNK CALCI");
		lo1.setBounds(30,220,500,300);
		lo1.setFont(lo1.getFont().deriveFont(23f));
		lo1.setForeground(Color.black);
		c11.add(lo1);
		c11.add(b13);
				b13.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				Bunkie me=new Bunkie();
			
				frame5.setVisible(false);
			}  
		}
		);  
		
											b14.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				TIt1 me=new TIt1();
				me.Fill();
				frame5.setVisible(false);
			}  
		}
		);  
		
		frame5.setLocationRelativeTo(null);
		frame5.setBounds(0,0,1500,1000);
        frame5.pack();
        frame5.setVisible(true);
		
	}
}


class Chem extends Branches
{
		public void Stream()
	{
		JFrame frame5 = new JFrame("Chemical");
        frame5.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		JPanel comps1 = (JPanel)frame5.getContentPane();
		JLabel c11 = new JLabel();
		c11.setIcon(new ImageIcon("chem.jpg"));
        comps1.add(c11);
		
		JLabel co=new JLabel("ROOM=505 OB");
		co.setBounds(150,0,500,300);
		co.setFont(co.getFont().deriveFont(23f));
		co.setBackground(Color.white);
		co.setForeground(Color.black);
		c11.add(co);
		JButton b14=new JButton();//bunk
		b14.setBounds(800,400, 10, 10);
		b14.setBackground(Color.cyan);
			JLabel lo2=new JLabel("TIMETABLE");
		lo2.setBounds(730,220,500,300);
		lo2.setForeground(Color.black);
		lo2.setFont(lo2.getFont().deriveFont(23f));
		c11.add(lo2);
		c11.add(b14);
		JButton b13=new JButton();//bunk
		b13.setBounds(100,400, 10, 10);
		b13.setBackground(Color.cyan);
		JLabel lo1=new JLabel("BUNK CALCI");
		lo1.setBounds(30,220,500,300);
		lo1.setFont(lo1.getFont().deriveFont(23f));
		lo1.setForeground(Color.black);
		c11.add(lo1);
		c11.add(b13);
				b13.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				Bunkie me=new Bunkie();
			
				frame5.setVisible(false);
			}  
		}
		);  
		
													b14.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				TChem me=new TChem();
				me.Fill();
				frame5.setVisible(false);
			}  
		}
		);  
		
		
		frame5.setLocationRelativeTo(null);
		frame5.setBounds(0,0,1000,1000);
        frame5.pack();
        frame5.setVisible(true);
		
	}
}

class Bio extends Branches
{
		public void Stream()
	{
		JFrame frame5 = new JFrame("Biomed");
		frame5.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		JPanel comps1 = (JPanel)frame5.getContentPane();
		JLabel c11 = new JLabel();
		c11.setIcon(new ImageIcon("bio.jpg"));
        comps1.add(c11);
		
		JLabel co=new JLabel("ROOM=307 OB");
		co.setBounds(150,0,500,300);
		co.setFont(co.getFont().deriveFont(23f));
		//co.setFont(Color.white);
		//co.setBackground(Color.cyan);
		co.setForeground(Color.black);
		c11.add(co);
		JButton b14=new JButton();//bunk
		b14.setBounds(800,400, 10, 10);
		b14.setBackground(Color.cyan);
			JLabel lo2=new JLabel("TIMETABLE");
		lo2.setBounds(730,220,500,300);
		lo2.setForeground(Color.black);
		lo2.setFont(lo2.getFont().deriveFont(23f));
		c11.add(lo2);
		c11.add(b14);
		JButton b13=new JButton();//bunk
		b13.setBounds(100,400, 10, 10);
		b13.setBackground(Color.cyan);
		JLabel lo1=new JLabel("BUNK CALCI");
		lo1.setBounds(30,220,500,300);
		lo1.setFont(lo1.getFont().deriveFont(23f));
		lo1.setForeground(Color.black);
		c11.add(lo1);
		c11.add(b13);
				b13.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				Bunkie me=new Bunkie();
			
				frame5.setVisible(false);
			}  
		}
		);  
		
															b14.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				TChem me=new TChem();
				me.Fill();
				frame5.setVisible(false);
			}  
		}
		);  
		
		frame5.setLocationRelativeTo(null);
		frame5.setBounds(0,0,1000,1000);
        frame5.pack();
        frame5.setVisible(true);
		
	}
}

class Bunkie
{
	Bunkie()
	{
		JFrame frame5 = new JFrame("Bunk Calci");
       frame5.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		JPanel comps1 = (JPanel)frame5.getContentPane();
		JLabel c11 = new JLabel();
		c11.setIcon(new ImageIcon("math.jpg"));
        comps1.add(c11);
		JLabel l1=new JLabel("Total lecs");
		l1.setBounds(300,0,1200,500);
		l1.setForeground(Color.black);
		l1.setFont(l1.getFont().deriveFont(23f));
		c11.add(l1);
		JTextField j1=new JTextField(50);
		j1.setBounds(800,225,500,30);
		j1.setFont(j1.getFont().deriveFont(23f));
		c11.add(j1);


		JTextField j2=new JTextField(50);
		j2.setBounds(800,275,500,30);
		j2.setFont(j1.getFont().deriveFont(23f));
		c11.add(j2);

		JLabel l2=new JLabel("Bunked Lecs");
		l2.setBounds(300,50,500,500);
		l2.setForeground(Color.black);
		l2.setFont(l1.getFont().deriveFont(23f));
		c11.add(l2);
		JButton b1=new JButton("SUBMIT");
		b1.setBounds(550, 500, 100, 40);
		c11.add(b1);
		JButton b2=new JButton("BACK ");
		b2.setBounds(700, 500, 100, 40);
		c11.add(b2);
								b2.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				Fra me=new Fra();
			//	me.Stream();
				frame5.setVisible(false);
			}  
		}
		);  
		
				b1.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				String s1,s2;
				s1=j1.getText();
				s2=j2.getText();
				float a=Float.parseFloat(s1);
				float b=Float.parseFloat(s2);
				//j2.setText(s1);
				System.out.println(a+b);
				
				String s=new String("s");
				PayOutofBounds c=new PayOutofBounds(s);
				float ef=c.See(a,b);
				if(ef<0)
					j1.setText("Attended Lecs cant be negative");
				else if(ef>100)
					j1.setText("Bunked cant be more than Attended Lecs");
				else
				{double d=Math.round((ef*100.0)/100.0);
				
				j1.setText("Total="+String.valueOf(d)+"%");}
				
			}  
		}
		);
		frame5.setLocationRelativeTo(null);
		frame5.setBounds(0,0,1000,1000);
        frame5.pack();
        frame5.setVisible(true);
	}
	}
abstract class Tt
{
		JLabel label = new JLabel();
				JTextField j2=new JTextField(24);
		JButton b1=new JButton("SUBMIT");
		JTextField j1=new JTextField(24);
		int x,y;
		Tt()
	{
		 JFrame frame = new JFrame("Timetable");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		JPanel panel = (JPanel)frame.getContentPane();
		
      
		 label.setIcon(new ImageIcon("tt.jpg"));
        panel.add(label);
				frame.setLocationRelativeTo(null);
        frame.pack();
		frame.setBounds(0,0,1500,1000);
        frame.setVisible(true);

		JLabel l1=new JLabel("Enter day of week");
		l1.setBounds(300,0,500,500);
		l1.setFont(l1.getFont().deriveFont(23f));
		label.add(l1);
		
		j1.setBounds(800,225,200,30);
		j1.setFont(j1.getFont().deriveFont(23f));
		j1.setText("Eg.1 for Monday");
		label.add(j1);
		JLabel l2=new JLabel("Enter time for lec");
		l2.setBounds(300,50,500,500);
		l2.setFont(l1.getFont().deriveFont(23f));
		label.add(l2);

		j2.setBounds(800,275,200,30);
		j2.setText("Eg.9 for 9-10 lec");
		j2.setFont(j1.getFont().deriveFont(23f));
		label.add(j2);
				
		b1.setBounds(550, 500, 100, 40);
		label.add(b1);
		JButton b2=new JButton("BACK ");
		b2.setBounds(700, 500, 100, 40);
		label.add(b2);
								b2.addActionListener(new ActionListener()
		{  
			public void actionPerformed(ActionEvent e)
			{
				
				Fra me=new Fra();
			//	me.Stream();
				frame.setVisible(false);
			}  
		}
		);  

					
}}
	
	

class TEx extends Tt
{
	void Fill()
	{			
		String tt[][]=new String[50][50];
		tt[1][1]="-";tt[1][2]="EMIC NP";tt[1][3]="EMIC NP";tt[1][4]="EDCI MS";
		tt[1][5]="DE/EDCI/EMIC/CTN";tt[1][6]="AK/MS/-/-";tt[1][7]="AM SA";tt[1][8]="AM (T)";
		tt[2][1]="-";tt[2][2]="A1/A2 EMIC NP";tt[2][3]="EMIC NP";tt[2][4]="EMIC NP";tt[2][5]="DE AK";
        tt[2][6]="DE AK ";tt[2][7]="A3/ DE/A4 OOPM ";tt[2][8]="AK";
        tt[3][1]="-";tt[3][2]="AM SA";tt[3][3]="CTN MK";tt[3][4]="DE AK";tt[3][5]="DE AK";
		tt[3][6]="EDCI MS"; tt[3][7]="EDCI/CTN"; tt[3][8]="MS/VB";
        tt[4][1]="-";tt[4][2]="AM SA";tt[4][3]="EDCI MS";tt[4][4]="CTN VB";tt[4][5]="OOPM/DE/EDCI";
        tt[4][6]="SBHATIA/NP";tt[4][7]="OOPM"; tt[4][8]="OOPM";tt[5][1]="-";tt[5][2]="AM SA";
		tt[5][3]="AM SA ";tt[5][4]="CTN VB";tt[5][5]="CTN VB";tt[5][6]="EDCI MS";tt[5][7]="EDCI/OOPM/DE ";   
        tt[5][8]="MS/-/SB";tt[1][0]="Break";tt[2][0]="Break";tt[3][0]="Break";tt[4][0]="Break";
		tt[5][0]="Break";
b1.addActionListener(new ActionListener()
			{
				public void actionPerformed(ActionEvent e)
				{
					if((j1.getText().equals(""))&&(j2.getText().equals("")))
					System.out.println("T");
					else 
					{String s1,s2;
					s1=j1.getText();
					s2=j2.getText();
					int a=Integer.parseInt(s1);
					int b=Integer.parseInt(s2);
					{if(((a<=0)&&(a<6))&&((b<8)&&(b>4)))
						{System.out.println("123");
						
						}
					
					else 
					{x=a;y=b;
								if(y==8)
				j1.setText(tt[x][1]);
			else if(y==9)
				j1.setText(tt[x][2]);
			else if(y==10)
				j1.setText(tt[x][3]);
			else if(y==11)
				j1.setText(tt[x][4]);
			else if(y==12)
				j1.setText(tt[x][0]);
			else if(y==1)
				j1.setText(tt[x][5]);
					else if(y==2)
				j1.setText(tt[x][6]);
			else if(y==3)
				j1.setText(tt[x][7]);
			else 
				j1.setText(tt[x][8]);
					System.out.println(x+y);
					}
					}
					}
			}}
					);
}}

class TCo2 extends Tt
{
	void Fill()
	{			
		String tt[][]=new String[50][50];
		tt[1][1]="-";tt[1][2]="DLDA TM";tt[1][3]="DATA/DLDA/OOPM/DATA";tt[1][4]="DATA/DLDA/OOPM/DATA";
		tt[1][5]="DLDA SB";tt[1][6]="DATA JRG";tt[1][7]="DLDA/-/-/-";tt[1][8]="DLDA/-/-/-";
		tt[2][1]="-";tt[2][2]="OOPM MD";tt[2][3]="DIS NM";tt[2][4]="DLDA TM";tt[2][5]="OOPM/ECCF/ECCF/DLDA";
        tt[2][6]="OOPM/ECCF/ECCF/DLDA";tt[2][7]="AM GT";tt[2][8]="AM(T) GT";
        tt[3][1]="-";tt[3][2]="OOPM MD";tt[3][3]="AM GT";tt[3][4]="DATA JKG";tt[3][5]="DLDA SB";
		tt[3][6]="ECCF VB"; tt[3][7]="ECCF/OOPM/DATA/ECCF"; tt[3][8]="ECCF/OOPM/DATA/ECCF";
        tt[4][1]="-";tt[4][2]="AM GT";tt[4][3]="DIS UB";tt[4][4]="ECCF KYR";tt[4][5]="DATA ASD";
        tt[4][6]="ECCF KYR";tt[4][7]="ECCF/OOPM/DATA/ECCF"; tt[4][8]="ECCF/OOPM/DATA/ECCF";tt[5][1]="-";
		tt[5][2]="AM GT";
		tt[5][3]="DIS UB";tt[5][4]="DATA ASD";tt[5][5]="DIS NM";tt[5][6]="ECCF KYR";tt[5][7]="-/DATA/-/-";   
        tt[5][8]="-/DATA/-/-";tt[1][0]="Break";tt[2][0]="Break";tt[3][0]="Break";tt[4][0]="Break";
		tt[5][0]="Break";
b1.addActionListener(new ActionListener()
			{
				public void actionPerformed(ActionEvent e)
				{
					if((j1.getText().equals(""))&&(j2.getText().equals("")))
					System.out.println("T");
					else 
					{String s1,s2;
					s1=j1.getText();
					s2=j2.getText();
					int a=Integer.parseInt(s1);
					int b=Integer.parseInt(s2);
					{if(((a<=0)&&(a<6))&&((b<8)&&(b>4)))
						{System.out.println("123");
						
						}
					
					else 
					{x=a;y=b;
								if(y==8)
				j1.setText(tt[x][1]);
			else if(y==9)
				j1.setText(tt[x][2]);
			else if(y==10)
				j1.setText(tt[x][3]);
			else if(y==11)
				j1.setText(tt[x][4]);
			else if(y==12)
				j1.setText(tt[x][0]);
			else if(y==1)
				j1.setText(tt[x][5]);
					else if(y==2)
				j1.setText(tt[x][6]);
			else if(y==3)
				j1.setText(tt[x][7]);
			else 
				j1.setText(tt[x][8]);
					System.out.println(x+y);
					}
					}
					}
			}}
					);
}}

class TCo1 extends Tt
{
	void Fill()
	{			
		String tt[][]=new String[50][50];
		tt[1][1]="-";tt[1][2]="AM PS";tt[1][3]="DIS VS";tt[1][4]="ECCF SB";
		tt[1][5]="DLDA VA";tt[1][6]="DATA ASD";tt[1][7]="ECCF/ECCF/DLDA/DATA";tt[1][8]="ECCF/ECCF/DLDA/DATA";
		tt[2][1]="-";tt[2][2]="-";tt[2][3]="AM PS";tt[2][4]="ECCF SB";tt[2][5]="DLDA MS";
        tt[2][6]="DATA AK ";tt[2][7]="-/OOPM/ECCF/DLDA ";tt[2][8]="-/OOPM/ECCF/DLDA";
        tt[3][1]="-";tt[3][2]="AM PS";tt[3][3]="OOPM SMS";tt[3][4]="DLDA MS";tt[3][5]="ECCF VB";
		tt[3][6]="DIS VS"; tt[3][7]="DATA/-/-/-"; tt[3][8]="DATA/-/-/-";
        tt[4][1]="AM PS";tt[4][2]="DIS UB";tt[4][3]="OOPM SMS";tt[4][4]="DATA ASD";tt[4][5]="OOPM/DLDA/DATA/OOPM";
        tt[4][6]="OOPM/DLDA/DATA/OOPM";tt[4][7]="-"; tt[4][8]="-";tt[5][1]="AM PS";tt[5][2]="DLDA VA";
		tt[5][3]="DLDA/DATA/OOPM/ECCF";tt[5][4]="DLDA/DATA/OOPM/ECCF";tt[5][5]="DIS UB";tt[5][6]="ECCF SB";tt[5][7]="DATA AK";   
        tt[5][8]="-";tt[1][0]="Break";tt[2][0]="Break";tt[3][0]="Break";tt[4][0]="Break";
		tt[5][0]="Break";
b1.addActionListener(new ActionListener()
			{
				public void actionPerformed(ActionEvent e)
				{
					if((j1.getText().equals(""))&&(j2.getText().equals("")))
					System.out.println("T");
					else 
					{String s1,s2;
					s1=j1.getText();
					s2=j2.getText();
					int a=Integer.parseInt(s1);
					int b=Integer.parseInt(s2);
					{if(((a<=0)&&(a<6))&&((b<8)&&(b>4)))
						{System.out.println("123");
						
						}
					
					else 
					{x=a;y=b;
								if(y==8)
				j1.setText(tt[x][1]);
			else if(y==9)
				j1.setText(tt[x][2]);
			else if(y==10)
				j1.setText(tt[x][3]);
			else if(y==11)
				j1.setText(tt[x][4]);
			else if(y==12)
				j1.setText(tt[x][0]);
			else if(y==1)
				j1.setText(tt[x][5]);
					else if(y==2)
				j1.setText(tt[x][6]);
			else if(y==3)
				j1.setText(tt[x][7]);
			else 
				j1.setText(tt[x][8]);
					System.out.println(x+y);
					}
					}
					}
			}}
					);
}}

class TIt1 extends Tt
{
	void Fill()
	{			
		String tt[][]=new String[50][50];
		tt[1][1]="AM(T)";tt[1][2]="JPL CA";tt[1][3]="PCE GK";tt[1][4]="DMS RM";
		tt[1][5]="DMS/JPL/PCE/-";tt[1][6]="DMS/JPL/PCE/-";tt[1][7]="PCE(T)";tt[1][8]="-";
		tt[2][1]="DSA GTT";tt[2][2]="DSA GTT";tt[2][3]="AM GT";tt[2][4]="LD MI";tt[2][5]="PCE GK";
        tt[2][6]="DMS MT";tt[2][7]="DMS/LD/PCE/- ";tt[2][8]="DMS/LD/PCE/-";
        tt[3][1]="DSA DI";tt[3][2]="DSA DI";tt[3][3]="JPL/DMS/LD/DSA";tt[3][4]="JPL/DMS/LD/DSA";tt[3][5]="LD HD";
		tt[3][6]="AM GT"; tt[3][7]="-/LD/JPL/-"; tt[3][8]="DATA/LD/JPL/-";
        tt[4][1]="DSA/DSA/-/-";tt[4][2]="DSA/DSA/-/-";tt[4][3]="DMS MT";tt[4][4]="PCE GK";tt[4][5]="AM GT";
        tt[4][6]="AM(T)";tt[4][7]="-/DMS/-/LD"; tt[4][8]="-/DMS/-/LD";tt[5][1]="AM GT";tt[5][2]="JPL CA";
		tt[5][3]="LD MI";tt[5][4]="DMS RM";tt[5][5]="-/JPL/DSA/PCE";tt[5][6]="-/JPL/DSA/PCE";tt[5][7]="PCE";   
        tt[5][8]="-";tt[1][0]="Break";tt[2][0]="Break";tt[3][0]="Break";tt[4][0]="Break";
		tt[5][0]="Break";
b1.addActionListener(new ActionListener()
			{
				public void actionPerformed(ActionEvent e)
				{
					if((j1.getText().equals(""))&&(j2.getText().equals("")))
					System.out.println("T");
					else 
					{String s1,s2;
					s1=j1.getText();
					s2=j2.getText();
					int a=Integer.parseInt(s1);
					int b=Integer.parseInt(s2);
					{if(((a<=0)&&(a<6))&&((b<8)&&(b>4)))
						{System.out.println("123");
						
						}
					
					else 
					{x=a;y=b;
								if(y==8)
				j1.setText(tt[x][1]);
			else if(y==9)
				j1.setText(tt[x][2]);
			else if(y==10)
				j1.setText(tt[x][3]);
			else if(y==11)
				j1.setText(tt[x][4]);
			else if(y==12)
				j1.setText(tt[x][0]);
			else if(y==1)
				j1.setText(tt[x][5]);
					else if(y==2)
				j1.setText(tt[x][6]);
			else if(y==3)
				j1.setText(tt[x][7]);
			else 
				j1.setText(tt[x][8]);
					System.out.println(x+y);
					}
					}
					}
			}}
					);
}}

class TChem extends Tt
{
	void Fill()
	{			
		String tt[][]=new String[50][50];
		tt[1][1]="-";tt[1][2]="AM ";tt[1][3]="Echem-1";tt[1][4]="CT RJ";
		tt[1][5]="PC RJ";tt[1][6]="ECHEM1/FFO/CET1/CELS";tt[1][7]="ECHEM1/FFO/CET1/CELS";tt[1][8]="ECHEM1/FFO/CET1/CELS";
		tt[2][1]="-";tt[2][2]="AM";tt[2][3]="ECHEM2";tt[2][4]="FFO SJP";tt[2][5]="CET1 AK";
        tt[2][6]="ECHEM1/FFO/PC/CELS ";tt[2][7]="ECHEM1/FFO/PC/CELS ";tt[2][8]="ECHEM1/FFO/PC/CELS";
        tt[3][1]="-";tt[3][2]="ECHEM1/FFO/CET1/CELS";tt[3][3]="ECHEM1/FFO/CET1/CELS";tt[3][4]="ECHEM1/FFO/CET1/CELS";
		tt[3][5]="CT RJ";
		tt[3][6]="FFO SJP"; tt[3][7]="PC EJ"; tt[3][8]="PC EJ";
        tt[4][1]="-";tt[4][2]="ECHEM1";tt[4][3]="AM ";tt[4][4]="CT RJ";tt[4][5]="CET1 AK";
        tt[4][6]="FFO SJP";tt[4][7]="PC EJ"; tt[4][8]="-";tt[5][1]="-";tt[5][2]="ECHEM1/FFO/CET1/CELS";
		tt[5][3]="ECHEM1/FFO/CET1/CELS";tt[5][4]="ECHEM1/FFO/CET1/CELS";tt[5][5]="CT RJ";tt[5][6]="ECHEM1";tt[5][7]="FFO SJP";   
        tt[5][8]="-";tt[1][0]="Break";tt[2][0]="Break";tt[3][0]="Break";tt[4][0]="Break";
		tt[5][0]="Break";
b1.addActionListener(new ActionListener()
			{
				public void actionPerformed(ActionEvent e)
				{
					if((j1.getText().equals(""))&&(j2.getText().equals("")))
					System.out.println("T");
					else 
					{String s1,s2;
					s1=j1.getText();
					s2=j2.getText();
					int a=Integer.parseInt(s1);
					int b=Integer.parseInt(s2);
					{if(((a<=0)&&(a<6))&&((b<8)&&(b>4)))
						{System.out.println("123");
						
						}
					
					else 
					{x=a;y=b;
								if(y==8)
				j1.setText(tt[x][1]);
			else if(y==9)
				j1.setText(tt[x][2]);
			else if(y==10)
				j1.setText(tt[x][3]);
			else if(y==11)
				j1.setText(tt[x][4]);
			else if(y==12)
				j1.setText(tt[x][0]);
			else if(y==1)
				j1.setText(tt[x][5]);
					else if(y==2)
				j1.setText(tt[x][6]);
			else if(y==3)
				j1.setText(tt[x][7]);
			else 
				j1.setText(tt[x][8]);
					System.out.println(x+y);
					}
					}
					}
			}}
					);
}}
		