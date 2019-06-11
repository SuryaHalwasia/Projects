<?php
// Start the session
session_start();
?>
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">

<style> 

h1
{
color:white;
font-family: comic sans MS;
font-size: 300%;
text-align: center;

}

h2
{
color:black;
font-family: comic sans MS;
font-size: 200%;
text-align: center;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 10 10;
  overflow: hidden;
  color:black;
  height: 100px;
  width=70px;
}

li {
  float: left;
  padding: 10px;
  margin-left:0px;
}


  
.btn1{
font-size:20px;
font-family:verdana;
color:black;
cursor: pointer;
  border-radius: 5px;
  text-align: center;
  padding: 13px 35px;
  border: none;
  
}
.btn1:hover{ background-color:black;
color:white;}
}
.a:hover{ background-color:black;
color:white;}
}

table {
  margin-left:0px;
  margin-right:300px;
  margin-top:0px;
  margin-bottom:300px;
  
  
  border-collapse: collapse;
  width: 50%;
  border-radius: 25px;
  border:300px; 
  background-color:url("bg1.jpg");
  position: absolute;
}

th, td {
  text-align: center;
  padding: 8px;
}

tr{background-color: #f2f2f2}

th {
  background-color:#3333cc;
  color: white;
}
body{
	background-image:url("bg3.jpg");
	background-color:#D3D3D3;
	background-repeat: no-repeat;
    background-size: cover;
	min-height: 50px;
	margin:0px;

}

input[type=text] {
  width: 30%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
  border-color: black;
  text-size:18px;
}	

</style>

<body>
<header>
<h1>
My profile
</h1>
</header>

<ul>
<li>
<h2><button class="btn1">Chatbot</button></h2>
<li>
<h2><button class="btn1"><a href="sae.php" style="color:black;text-decoration:none;">Personal Goals</a></button></h2>
</li>
<li>
<h2><button class="btn1">Record Expenses</button></h2>
</li>
<li>
<h2><button class="btn1">Bill</button></h2>
</li>
<li>
<h2><button class="btn1">Estimation</button></h2>
</li>
</ul>


<form method="post">
<?php  
$db = mysqli_connect("localhost", "root", '', "finance");
 # Prepare the SELECT Query
 $username=$_SESSION["username"];
  $selectSQL = "SELECT Name, ubudget_n, ubudget_w, ubudget_s FROM user where uname='$username'" ;
 # Execute the SELECT Query
 $selectRes = mysqli_query( $db,$selectSQL );
 ?>
<br><br><center><table border="10" width="500px" height="300px" style="background:black;color:black;font-family:comic sans MS; font-size:25px;">
  <thead>
    <tr>
      <th height="30px" >Name</th>
	  <?php
		while( $row = mysqli_fetch_assoc( $selectRes ) ){
          echo "<th>{$row["Name"]}</th>";
        }
      ?>
	  <th>Update</th>
	</tr>
	<tr>
	  <td height="30px">Need %</td>
	  <?php
	  $selectRes = mysqli_query( $db,$selectSQL );
		while( $row = mysqli_fetch_assoc( $selectRes ) ){
          echo "<td>{$row["ubudget_n"]}</td>";
        }
		?>
		<td><font color="yellow"><input type="text" onchange="ne()" name="need" id="need"></td>
	</tr>
	
	<tr>
	<td height="30px">Want %</td>
	  <?php
	  $selectRes = mysqli_query( $db,$selectSQL );
		while( $row = mysqli_fetch_assoc( $selectRes ) ){
          echo "<td>{$row["ubudget_w"]}</td>";
        }
		?>
		<td><font color="yellow"><input type="text" name="want" onchange="we" id="want"></td>
		</font>
	</tr>
	
	<tr>
	<td height="30px">Savings %</td>
	  <?php
	  $selectRes = mysqli_query( $db,$selectSQL );
		while( $row = mysqli_fetch_assoc( $selectRes ) ){
          echo "<td>{$row["ubudget_s"]}</td>";
        }
		?>
		<td><font color="yellow"><input type="text" name="save" onchange="se" id="save"></td>
	</tr>
	
	
  </thead>
  </table>
  <div>
  <h1><input type="submit" name="submit" class="btn1"></h1>
  </div>
  <?php 
	
	$db = mysqli_connect("localhost","root", "", "finance"); // Establishing Connection with Server
	
    if (isset($_POST['submit'])) { //to check if the form was submitted
        $need= $_POST['need'];
		$want= $_POST['want'];
		$save= $_POST['save'];
    
	$query = "update user set ubudget_n='$need',ubudget_w='$want',ubudget_s='$save' where uname='$username'";
	if(mysqli_query($db, $query)){
		echo "<br/><br/><span>Data Updated successfully...!!</span>";
	}
	else
	{
		echo "error:".$query."<br>".mysqli_error($db);
		}
	}
?>

 </div> 
 </div>
</form>
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


</body>
</html>



