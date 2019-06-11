
<!DOCTYPE html>
<html>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<meta charset="utf-8">
<meta name="viewport"content="width=device-width, minimum-scale=1.0, initial-scale=1">
<style>
#headbb{width:1250px;height:250px;}
body {overflow-x:hidden;
background-image:url("bgr.png") ; 
width:1200px;
}
#one{position:relative;left:300px;background: rgba(10, 0, 0, 0.5);width:600px;height:600px;font-family: Arial, Helvetica, sans-serif;}
.container{
position:realtive;
}
.left{
position: absolute;
right:70px;
padding-left:20px;
padding-right:20px;
padding-top:10px;}
form.example input[type=text] {
    font-size: 17px;
    border: 1px solid grey;
    float: left;
    width: 68%;
    background: #f1f1f1;
}
form.example button {
   float:right;
    width: 20%;
	
    padding: 3px;
    background: blue;
}
form.example::after {
    content: "";
    clear: both;
    display: table;
}
.navbar {width:1250px;
    overflow: hidden;
    background-color: #333;
    font-family: Arial, Helvetica, sans-serif;
}
.navbar a {
    float: left;
    font-size: 16px;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}
.dropdown {
    float: left;
    overflow: hidden;
}
.dropdown .dropbtn {
    cursor: pointer;
    font-size: 16px;    
    border: none;
    outline: none;
    color: white;
    padding: 14px 16px;
    background-color: inherit;
    font-family: inherit;
    margin: 0;
}
.navbar a:hover, .dropdown:hover .dropbtn, .dropbtn:focus {
    background-color: red;
}
.dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
}
.dropdown-content a {
    float: none;
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    text-align: left;
}
.dropdown-content a:hover {
    background-color: #ddd;
}
.show {
    display: block;
}
.mySlides {display: none;}
img {vertical-align: middle;}
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}
.text {
  color:#B6F9F3;
  font-size: 30px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}
.dot {
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}
.active {
  background-color: #717171;
}
/* Fading animation */
.fade {
  -webkit-animation-name: fade;
  -webkit-animation-duration: 1.5s;
  animation-name: fade;
  animation-duration: 1.5s;
}
@-webkit-keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}
@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}
/* On smaller screens, decrease text size */
@media only screen and (max-width: 300px) {
  .text {font-size: 30px}
}
.column {
    float: left;
    width: 50%;
    padding: 30px;
}
/* Clear floats after the columns */
.row:after {
    content: "";
    display: table;
    clear: both;
}
/* Style the buttons */
.btn {
    border: none;
    outline: none;
    padding: 12px 16px;
    background-color: #881409;
    cursor: pointer;
}
.btn:hover {
    background-color: #CE2919;
}
.btn.active {
    background-color: #CE2919;
    color: white;
}
h2 a{color:white;
text-decoration:none;}
.fa {
  padding: 20px;
  font-size: 30px;
  width: 30px;
  text-align: center;
  text-decoration: none;
  margin: 5px 2px;
  border-radius: 50%;
}
.fa:hover {
    opacity: 0.7;
}
.fa-facebook {
  background: #3B5998;
  color: white;
}
.fa-twitter {
  background: #55ACEE;
  color: white;
}
.fa-google {
  background: #dd4b39;
  color: white;
}
table{
text-align:center;
color:yellow;
}
th{
font-size:30;
color:white;}
footer{width:1250px;
background-color:#333;
}
h3{
color:white;
}
@media only screen and (max-width: 415px) {
body {width:360px;overflow-x:hidden;
background-image:url("bgr.png") ; 
}header{width:360px}
#one{position:relative;left:30px;background: rgba(10, 0, 0, 0.5);width:300px;height:500px;font-family: Arial, Helvetica, sans-serif;}
	#headbb{width:380px;height:150px;}
	.navbar {width:380px;
    overflow: hidden;
    background-color: #333;
    font-family: Arial, Helvetica, sans-serif;
}
.navbar a {
    float: left;
    font-size: 15px;
    color: white;
    text-align: center;
    padding: 8px 8px;
    text-decoration: none;
}
.left{
position: absolute;
padding-left:8px;
padding-right:8px;
padding-top:10px;}
footer{width:360px;
background-color:#333;
}
	}
	@media only screen and (min-width: 700px) {
body {width:700px;
background-image:url("bgr.png") ; 
overflow-x:hidden;
}header{width:700px}
#one{position:relative;left:100px;background: rgba(10, 0, 0, 0.5);width:500px;height:500px;font-family: Arial, Helvetica, sans-serif;}
	#headbb{width:700px;height:200px;}
	.navbar {width:700px;
    overflow: hidden;
    background-color: #333;
    font-family: Arial, Helvetica, sans-serif;
}
.navbar a {
    float: left;
    font-size: 15px;
    color: white;
    text-align: center;
    padding: 8px 8px;
    text-decoration: none;
}
.left{
position: absolute;
padding-left:8px;
padding-right:8px;
padding-top:10px;}
footer{width:700px;
background-color:#333;
}
	}
@media only screen and (min-width:1200px) {
body {width:1250px;overflow-x:hidden;
background-image:url("bgr.png") ; 
}header{width:1250px}
#one{position:relative;left:300px;background: rgba(10, 0, 0, 0.5);width:600px;height:600px;font-family: Arial, Helvetica, sans-serif;}
	#headbb{width:1250px;height:250px;}
	.navbar {width:1250px;
    overflow: hidden;
    background-color: #333;
    font-family: Arial, Helvetica, sans-serif;
}
.navbar a {
    float: left;
    font-size: 15px;
    color: white;
    text-align: center;
    padding: 8px 8px;
    text-decoration: none;
}
.left{
position: absolute;
padding-left:8px;
padding-right:8px;
padding-top:10px;}
footer{width:1250px;
background-color:#333;
}
	}
</style>
<body>
<header><div class="container">
       <img src="bghhh.jpg" id="headbb">
</div>
        <div class="navbar">
  <a href="index.html">Home</a>
  <a href="about_us.html">About Us</a>
  <a href="final_reg.php#contact">Contact Us</a>
  <a href="final_login.php">Login</a>
</div>
</header>
</br></br>
<section id="two">
<a href="final_login.php"><font face=" Bookman" color="white" size="5"><B>ALREADY REGISTERED...</B></font><br></a>
</section>
<section id="one" >

	<form method="post" action="final_reg.php">
	<font color="#FFCDF5" size="4">
	<?php include('errors.php'); ?></font>
	<font color="#FFCDF5" size="10"><b>
		<CENTER><legend><span id=cd >WELCOME!</span></legend></CENTER></font>
		<font color="#D5CFFF" size="5">
		<span id=ab >Name :</span> </br><input type="text" name="name" value="<?php echo $name; ?>" style="background: rgba(0, 0, 0, 0.5);display: inline-block;
    border: none;width:70%;padding: 7px;color:white;">
		</br>
		<span id=ab >Username  :</span></br> <input type="text" name="username" value="<?php echo $username; ?>" style="background: rgba(0, 0, 0, 0.5);display: inline-block;
    border: none;width:70%;padding: 7px;color:white;">
		</br>
		<span id=ab >Email id   :</span> </br> <input type="email" name="email" value="<?php echo $email; ?>" style="background: rgba(0, 0, 0, 0.5);display: inline-block;
    border: none;width:70%;padding: 7px;color:white;">
		</br>
		
		<span id=ab >Phone no.  :</span> </br><input type="tel" name="phoneno"  required  value="<?php echo $phoneno; ?>" style="background: rgba(0, 0, 0, 0.5);display: inline-block;
    border: none;width:70%;padding: 7px;color:white;">
		</br>
		<span id=ab >Password   :</span></br> <input type="password" name="password_1" style="background: rgba(0, 0, 0, 0.5);display: inline-block;
    border: none;width:70%;padding: 7px;color:white;">
		</br>
		<span id=ab >Confirm Password   :</span> </br><input type="password" name="password_2" style="background: rgba(0, 0, 0, 0.5);display: inline-block;
    border: none;width:70%;padding: 7px;color:white;">
		</br></br>
	</font></b>
		<center><button style="background: rgba(0, 0, 0, 0.5);color:white;width:50%;padding:7px;"type="submit" align="center" name="reg_user">REGISTER</button></center>
	
</form>
</section></br><br><br>

<footer><br><br><br>
<table style="width:100%">
<tr>
<th>Related links</th>
<th>About Us</th>
<th>Other Options</th>
</tr>
<tr>
<td><a href="https://festpav.com" target="_blank" style="text-decoration:none;color:yellow;">festpav</td></a>
<td><a href="about_us.html#mahima"  style="text-decoration:none;color:yellow;">Hiba Hussain</td></tr></a>
<tr>
<td><a href="https://www.foodpanda.in" target="_blank" style="text-decoration:none;color:yellow;">FoodPanda</td></a>
<td><a href="about_us.html#komal"  style="text-decoration:none;color:yellow;">Komal Aswani</td></a>
<td>Copyrights link</td></tr>
<tr>
<td><a href="https://www.trivago.in" target="_blank" style="text-decoration:none;color:yellow;">Trivago</td></a>
<td><a href="about_us.html#hiba"  style="text-decoration:none;color:yellow;">Mahima Gupta</td></a>
<td>Blog</td></tr>

</table>
<div id='contact'><h3>Contact Us</h3>
<a href="https://www.facebook.com/hiba.hussain.1257"target="_blank" class="fa fa-facebook"></a>
<a href="#" class="fa fa-twitter"></a>
<a href="#" class="fa fa-google"></a><br>
<center><h3>@Copyrights 2018</h3></center>
</footer>
<script>
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}
window.onclick = function(e) {
  if (!e.target.matches('.dropbtn')) {
    var myDropdown = document.getElementById("myDropdown");
      if (myDropdown.classList.contains('show')) {
        myDropdown.classList.remove('show');
      }
  }
}
var slideIndex = 0;
showSlides();
function showSlides() {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("dot");
    for (i = 0; i < slides.length; i++) {
       slides[i].style.display = "none";  
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}    
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";  
    dots[slideIndex-1].className += " active";
    setTimeout(showSlides, 2000); // Change image every 2 seconds
}
var elements = document.getElementsByClassName("column");
// Declare a loop variable
var i;
// List View
function listView() {
  for (i = 0; i < elements.length; i++) {
    elements[i].style.width = "100%";
  }
}
// Grid View
function gridView() {
  for (i = 0; i < elements.length; i++) {
    elements[i].style.width = "30%";
  }
}
/* Optional: Add active class to the current button (highlight it) */
var container = document.getElementById("btnContainer");
var btns = container.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function(){
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}
</script>
</body>
</html>
