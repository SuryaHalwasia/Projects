<!DOCTYPE html>
<html>
<head>
  <title>Registration system PHP and MySQL</title>
  <link rel="stylesheet" type="text/css" href="style.css">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
  body{
	   background-image:url("bg3.jpg");
	      background-repeat: no-repeat;
  background-size: cover;
	   
  }
  ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
  height: 57px;
}

li {
  float: right;
}
#fin{
	position: relative;
	right: 700px;
	font-size: 18px;
	color:red;
}
li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover:not(.active) {
  background-color: #111;
}

.active {
  background-color: #4CAF50;
}


.header {
  width: 50%;
  margin: 50px auto 0px;
  color: white;
  background: black;
  text-align: center;
  border: 1px solid #B0C4DE;
  border-bottom: none;
  border-radius: 10px 10px 0px 0px;
  padding: 20px;
}

form, .content {
  width: 50%;
  margin: 0px auto;
  padding: 20px;
  border: 1px solid #B0C4DE;
  background: rgba(200,200,200,0.6);
  border-radius: 0px 0px 10px 10px;
}
.input-group {
  margin: 10px 0px 10px 0px;
}
.input-group label {
  display: block;
  text-align: left;
  margin: 3px;
  color:#581845;
  font-size:25px;
  font-family:"Comic Sans MS";
}
.input-group input {
  height: 30px;
  width: 93%;
  padding: 5px 10px;
  font-size: 16px;
  border-radius: 5px;
  border: 1px solid gray;
}
.btn {
  padding: 10px;
  font-size: 25px;
  color: white;
  background: black;
  border: none;
  border-radius: 5px;
}
  </style>
</head>
<body>
<header>

<ul>
	<img src="lo.jpg" alt="logo" style="height: 57px" />
  <li><a href="login.php">Login</a></li>
  <li><a href="index.html">Home</a></li>
  <li id="fin"><a href=""> FINANCE MANAGER</a></li>
</ul>


</header>

  <div class="header">
  	<h2>Register</h2>
  </div>
	
  <form method="post" action="regf.php">
<div class="input-group">
  	  <label>Name</label>
  	  <input type="text" name="name" >
  	</div>
  	<div class="input-group">
  	  <label>Your Username</label>
  	  <input type="text" name="username" >
  	</div>
  	<div class="input-group">
  	  <label>Password</label>
  	  <input type="password" name="ipass" >
  	</div>
	<div class="input-group">
  	  <label>Family username</label>
  	  <input type="text" name="fname" >
  	</div>
	<div class="input-group">
  	  <label>Family password</label>
  	  <input type="password" name="fpass" >
  	</div>
	<div class="input-group">
  	  <label>Contact</label>
  	  <input type="email" name="email" >
  	</div>
  	<div class="input-group">
  	  <label>Monthly Salary</label>
  	  <input type="decimal" name="salary" >
  	</div>
	<div class="input-group">
  	  <label>The budget alloted to Need is 50%, Want is 30% and Savings is 20%.. If you wish to change click</label>
	  
	
<div id="welcomeDiv"   > 
  	  <label>Budget Distribution</label>
  	  <label>Need</label><input type="decimal" id="need"name="need" onchange="ne()">
  <label>Want</label><input type="decimal"  id="want" name="want" onchange="we()">
   <label>Savings</label><input type="decimal" id="save" name="savings" onchange="se()">
  	</div>
  	<div class="input-group">
  	  <button type="submit" class="btn" name="reg_user" >Register</button>
  	</div>
  	<p>
  		Already a member?Sign in
  	</p></div>
  </form>
  <?php


// connect to the database
$db = mysqli_connect('localhost', 'root', '', 'finance');

// REGISTER USER
if (isset($_POST['reg_user'])) {
	 $username = mysqli_real_escape_string($db, $_POST['username']);
	 $fusername = mysqli_real_escape_string($db, $_POST['fname']);
  $name = mysqli_real_escape_string($db, $_POST['name']);
    $email = mysqli_real_escape_string($db, $_POST['email']);
  $password = mysqli_real_escape_string($db, $_POST['ipass']);
    $fpassword = mysqli_real_escape_string($db, $_POST['fpass']);
	    $salary= mysqli_real_escape_string($db, $_POST['salary']);
		$need= mysqli_real_escape_string($db, $_POST['need']);
		$want= mysqli_real_escape_string($db, $_POST['want']);
		$savings= mysqli_real_escape_string($db, $_POST['savings']);
		 if ($need==NULL || $want==NULL||$savings==NULL) { // if user exists
 
      $query = "INSERT INTO user (Name,uname,upassword,fname,fpassword,Contact,ubudget_n,ubudget_w,ubudget_s,fbudget_n,fbudget_w,fbudget_s,salary) 
  			  VALUES('$name','$username','$password','$fusername','$fpassword','$email',50,30,20,50,30,20,'$salary')";
			   $query1 = "INSERT INTO expenditure (uname,salary) 
  			  VALUES('$username','$salary')";
	mysqli_query($db, $query1);
  	mysqli_query($db, $query);
  
    }
else
{
	 $query = "INSERT INTO user (Name,uname,upassword,fname,fpassword,Contact,ubudget_n,ubudget_w,ubudget_s,fbudget_n,fbudget_w,fbudget_s,salary) 
  			  VALUES('name','$username','$password','$fusername','$fpassword','$email',$need,$want,$savings,50,30,20,'$salary')";
  	mysqli_query($db, $query);
	$query1 = "INSERT INTO expenditure (uname,salary) 
  			  VALUES('$username','$salary')";
	mysqli_query($db, $query1);
}
  	 header('location: login.php');
}
?>
<script>
var n=document.getElementById("need");
var s=document.getElementById("save");
var w=document.getElementById("want");
n.value="50";
s.value="20";
w.value="30";
function ne(){
	if(n.value>=100){
		n.value=100;
		s.value=0;
		w.value=0;
	}
	else
	s.value=100-n.value-w.value;
		if(s.value<0)
		{
			s.value=0;
			w.value=100-n.value;
		}
	}
function we(){
		if(w.value>=100){
		w.value=100;
		s.value=0;
		n.value=0;
	}
	else
	s.value=100-n.value-w.value;
		if(s.value<0)
		{
			s.value=0;
			n.value=100-w.value;
		}
}
function se(){
	
		if(s.value>=100){
		s.value=100;
		n.value=0;
		w.value=0;
	}
	else n.value=100-w.value-s.value;
			if(n.value<0)
		{
			n.value=0;
			w.value=100-s.value;
		}
}
</script>
</body>
</html>