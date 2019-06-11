<?php
// Start the session
session_start();
?>
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
  <li><a href="index.html">Home</a></li>
  <li id="fin"><a href="">SAVINGS MANAGER</a></li>
</ul>

</header>
<BR /><BR />

	
   <form method="post" action="sae.php">
<div class="input-group">
  	  <label>Goal of saving</label>
  	  <input type="text" name="goal" >
  	</div>
  	<div class="input-group">
  	  <label>Amount</label>
  	  <input type="text" name="amount" id="amt">
  	</div>
  	<div class="input-group">
  	  <label>Time Period in Months</label>
  	  <input type="text" name="tt" id="tt">
  	</div>
<div class="input-group">
  	  <button  class="btn" name="goal1"  >Submit</button>
	  
  	</div>

  </form>
 
<script>
var t=document.getElementById("tt");
var a=document.getElementById("amt");
function re(){
	var save=a.value/t.value;
alert(save);
	}
</script>
<?php 
$db = mysqli_connect('localhost', 'root', '', 'finance');
if (isset($_POST['goal1'])) {
	 $username =$_SESSION["username"];
	 $goal = mysqli_real_escape_string($db, $_POST['goal']);
	 $amount = mysqli_real_escape_string($db, $_POST['amount']);
	 $tt = mysqli_real_escape_string($db, $_POST['tt']);
	 $now=$amount/$tt;
	 echo $now;
	  $query1 = "INSERT INTO goal (uname,Goal,Amount,Time_period,Amp) 
  			  VALUES('$username','$goal','$amount','$tt','$now')";
mysqli_query($db, $query1);
$query = "SELECT Goal FROM goal WHERE uname='$username'";
  	$results = mysqli_query($db, $query);
$row = mysqli_fetch_array($results);
$goal = $row['Goal'];


$queryt = "SELECT Time_period FROM goal WHERE uname='$username'";
  	$resultst = mysqli_query($db, $queryt);
$row = mysqli_fetch_array($resultst);
$tt= $row['Time_period'];


$_SESSION["goal"] = "$goal";
$_SESSION["amount"] = "$amount";
$_SESSION["amount1"] = "$amount";

$_SESSION["tt"] = "$tt";
$_SESSION["now"] = "$now";
header('location: next.php');
}
?>
</body>
</html>