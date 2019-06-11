<?php
// Start the session
session_start();
?>
<!DOCTYPE html>
<html>
<head>
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
  	<h2>Login</h2>
  </div>
	 
  <form method="post" action="login.php">
  	
  	<div class="input-group">
  		<label>Username</label>
  		<input type="text" name="username" >
  	</div>
  	<div class="input-group">
  		<label>Password</label>
  		<input type="password" name="password">
  	</div>
  	<div class="input-group">
  		<button type="submit" class="btn" name="login_user">Login</button>
  	</div>
  	<p>
  		Not yet a member? <a href="regf.php">Sign up</a>
  	</p>
  </form>
  <?php
  $db = mysqli_connect('localhost', 'root', '', 'finance');
  if (isset($_POST['login_user'])) {
  $username = mysqli_real_escape_string($db, $_POST['username']);
  $password = mysqli_real_escape_string($db, $_POST['password']);

  	$query = "SELECT * FROM user WHERE uname='$username' AND upassword='$password'";
  	$results = mysqli_query($db, $query);
	$queryf = "SELECT food FROM exp_categories WHERE uname='$username'";
  	$resultf = mysqli_query($db, $queryf);
$row = mysqli_fetch_array($resultf);
$food = $row['food'];

$queryc = "SELECT clothes FROM exp_categories WHERE uname='$username'";
  	$resultc = mysqli_query($db, $queryc);
$row = mysqli_fetch_array($resultc);
$clothes = $row['clothes'];


$querys = "SELECT savings FROM expenditure WHERE uname='$username'";
  	$resultss = mysqli_query($db, $querys);
$row = mysqli_fetch_array($resultss);
$savings = $row['savings'];

  	if (mysqli_num_rows($results) == 1) {
$_SESSION["username"] = "$username";

  	}
$_SESSION["food"] = "$food";
$_SESSION["clothes"] = "$clothes";
$_SESSION["savings"] = "$savings";
 header('location: final.php');
}
  ?>
</body>
</html>
