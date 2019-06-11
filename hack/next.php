<?php
// Start the session
session_start();
?>
<!DOCTYPE html>
<html>
<head>
  <title>Registration system PHP and MySQL</title>
  <link rel="stylesheet" type="text/css" href="style.css">
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
 

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
  <li id="fin"><a href="">FINANCE MANAGER</a></li>
</ul>

</header>
  <div class="header">
  	<h2>SAVINGS MANAGER</h2>
  </div>
	
	
   <form method="post">
<div class="input-group" >
  	  <label>Goal: </label>
	  <label><?php echo $_SESSION["goal"] ?></label>

	 
  	</div>
  	<div class="input-group"  >
	
  	  <label>Savings: </label>
  	   <label><?php echo $_SESSION["savings"] ?></label>
  	</div>
	<div class="input-group"  >
	
  	  <label>Amount left: </label>
  	   <label><?php echo $_SESSION["amount1"] ?></label>
  	</div>
  	<div class="input-group" >
  	  <label>Time Period in Months</label>
  	   <label><?php echo $_SESSION["tt"] ?></label>
  	</div>
<div class="input-group">
  	  <button  class="btn" name="pay"  id='p'>Pay</button>
	   
	 
  	</div>

  </form>
 <div class="container">
  <h2>Progress Bar With Label</h2>
  <?php 
  if (isset($_POST['pay'])) {
	 
  $savings=$_SESSION["savings"];
  $now=$_SESSION["now"];
 
 $amount=$_SESSION["amount"];
  $num=$amount-$now;
  $now=$now+$now;
 $_SESSION["amount1"]=$num;
echo $num;

  $total=$now/$amount;
  
  $f=$total*100;
  $_SESSION["f"]=$f;
  
  }
  ?>
  <div class="progress">
    <div class="progress-bar" role="progressbar"  aria-valuemin="0" aria-valuemax="100" style="width:<?php echo $_SESSION["f"]?>%;">
      <?php echo $f?>
    </div>
  </div>
</div>

</body>
</html>