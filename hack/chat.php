<?php
session_start();
?><html lang="en">
<head>
	<title>convForm - example</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, minimum-scale=1">
	<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
	<link rel="stylesheet" type="text/css" href="jquery.convform.css">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
	<link rel="stylesheet" type="text/css" href="demo.css">
</head>
<style>
body{
	   background-image:url("bg4.jpg");
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

</style>
<body>
<header>

<ul>
	<img src="lo.jpg" alt="logo" style="height: 57px" />
  <li><a href="index.html">Home</a></li>
  <li id="fin"><a href=""> FINANCE MANAGER</a></li>
</ul>


</header>

	<section id="demo">
	    <div class="vertical-align">
	        <div class="container">
	            <div class="row">
	                <div class="col-sm-6 col-sm-offset-3 col-xs-offset-0">
	                    <div class="card no-border">
	                        <div id="chat" class="conv-form-wrapper">
	                            <form action="" method="GET" class="hidden">
	                                <select data-conv-question="Welcome  <?php  echo $_SESSION["username"];?>! Do you have any questions?" name="first-question">
	                                    <option value="yes">Yes</option>
	                                   
	                                </select>
	                             <select name="programmer" data-callback="storeState" data-conv-question="Select">
									<option value="month">Monthly Expenses</option>
	                                    <option value="categ">Category-Wise</option>
	                                    <option value="save">Total savings</option>
										<option value="prof">Professional Advice</option>
	                                </select>
	                                <div data-conv-fork="programmer">
	                                    <div data-conv-case="month">
	                                        <input type="text" data-conv-question="Your monthly expenses are Rs." data-no-answer="true">
	                                    </div>
										<div data-conv-case="save">
	                                        <input type="text" data-conv-question="Your savings are Rs. <?php  echo $_SESSION["savings"];?>" data-no-answer="true">
	                                    </div>
									<div data-conv-case="prof">
									<select data-conv-question="Choose the experts to contact">
											<option value="prof" data-callback="prof">Contact investment agents</option>
											<option value="managers" data-callback="managers">Contact Mutual fund managers</option>
									</select>
									</div>
	                                    <div data-conv-case="categ">
		                                    <select name="thought" data-callback="storeState" data-conv-question="Select a category ">
		                                    	<option value="food">Food</option>
		                                    	<option value="cloth">Clothes.</option>
		                                    	<option value="bills">Bills</option>
		                                    	<option value="book">Books</option>
		                                    	<option value="movies">Movies</option>
		                                    	<option value="misc">Miscellanous</option>
		                                    </select>
											<div data-conv-fork="thought">
												<div data-conv-case="food">
	                                        <input type="text" data-conv-question="Your expenses on food are Rs. <?php  echo $_SESSION["food"];?>" data-no-answer="true">
												</div>
												<div data-conv-case="cloth">
	                                        <input type="text" data-conv-question="Your expenses on clothes are Rs. <?php  echo $_SESSION["clothes"];?>" data-no-answer="true">
												</div>
												<div data-conv-case="book">
												<input type="book" data-conv-question="Your expenses on books are Rs." data-no-answer="true">
												</div>
												<div data-conv-case="bills">
	                                        <input type="text" data-conv-question="Your expenses on bills are Rs." data-no-answer="true">
												</div>
												<div data-conv-case="movies">
												<input type="movies" data-conv-question="Your expenses on movies are Rs." data-no-answer="true">
												</div>
												<div data-conv-case="misc">
	                                        <input type="text" data-conv-question="Your miscellanious expenses are Rs." data-no-answer="true">
												</div>
											</div>
											
										</div>
	                                  </div>
	                        <!--        <input type="text" data-conv-question="Please select any of the options to continue." data-no-answer="true">
	                                <select name="multi[]" data-callback="storeState" data-conv-question="Select" multiple>
	                                    <option value="month">Monthly Expenses</option>
	                                    <option value="categ">Category-Wise</option>
	                                    <option value="save">Total savings</option>
	                                </select>
	                            <!--    <select name="programmer" data-callback="storeState" data-conv-question="So, are you a programmer? (this question will fork the conversation based on your answer)">
	                                    <option value="yes">Yes</option>
	                                    <option value="no">No</option>
	                                </select>
	                                <div data-conv-fork="multi[]">
	                                    <div data-conv-case="month">
	                                        <input type="text" data-conv-question="Your monthly expenses are Rs." data-no-answer="true">
	                                    </div>
	             
	                                    <div data-conv-case="categ">
		                                    <select name="thought" data-conv-question="Select a category ">
		                                    	<option value="food">Food</option>
		                                    	<option value="cloth">Clothes.</option>
		                                    	<option value="bills">Bills</option>
		                                    	<option value="book">Books</option>
		                                    	<option value="movies">Movies</option>
		                                    	<option value="misc">Miscellanous</option>
		                                    </select>
	                                    </div>
	                                    <div data-conv-case="save">
	                                    	 <input type="text" data-conv-question="Your Total savings are Rs." data-no-answer="true">
	                                    </div>	                                    
	                                </div>
	                                <input type="text" data-conv-question="convForm also supports regex patterns. Look:" data-no-answer="true">
	                                <input data-conv-question="Type in your e-mail" data-pattern="^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$" id="email" type="email" name="email" required placeholder="What's your e-mail?">
	                                <input data-conv-question="Now tell me a secret (like a password)" type="password" data-minlength="6" id="senha" name="password" required placeholder="password">
							-->	
	                               <!-- <select name="callbackTest" data-conv-question="You can do some cool things with callback functions. Want to rollback to the 'programmer' question before?">
	                                    <option value="yes" data-callback="rollback">Yes</option>
	                                    <option value="no" data-callback="restore">No</option>
	                                </select>
	                            -->    <select data-conv-question="This is it! If you need help, please contact us" id="">
	                                    <option value="">Awesome!</option>
	                                </select>
	                            </form>
	                        </div>
	                    </div>
	                </div>
	            </div>
	        </div>
	    </div>
	</section>
	<script type="text/javascript" src="jquery-1.12.3.min.js"></script>
	<script type="text/javascript" src="https://eduardotkoller.github.io/convForm/jquery-1.12.3.min.js"></script>
	<script type="text/javascript" src="jquery.convform.js"></script>

	<script>
		function google(stateWrapper, ready) {
			window.open("https://google.com");
			ready();
		}
		function prof(stateWrapper, ready) {
			window.open("https://www.justdial.com/Mumbai/Investment-Agents/nct-10276141");
			ready();
		}
		function managers(stateWrapper, ready) {
			window.open("https://www.justdial.com/Mumbai/Mutual-Fund-Agents/nct-10334024");
			ready();
		}
		function bing(stateWrapper, ready) {
			window.open("https://bing.com");
			ready();
		}
		var rollbackTo = false;
		var originalState = false;
		function storeState(stateWrapper, ready) {
			rollbackTo = stateWrapper.current;
			console.log("storeState called: ",rollbackTo);
			ready();
		}
		function rollback(stateWrapper, ready) {
			console.log("rollback called: ", rollbackTo, originalState);
			console.log("answers at the time of user input: ", stateWrapper.answers);
			if(rollbackTo!=false) {
				if(originalState==false) {
					originalState = stateWrapper.current.next;
						console.log('stored original state');
				}
				stateWrapper.current.next = rollbackTo;
				console.log('changed current.next to rollbackTo');
			}
			ready();
		}
		function restore(stateWrapper, ready) {
			if(originalState != false) {
				stateWrapper.current.next = originalState;
				console.log('changed current.next to originalState');
			}
			ready();
		}
	</script>
	<script>
		jQuery(function($){
			convForm = $('#chat').convform({selectInputStyle: 'disable'});
			console.log(convForm);
		});
	</script>
</body>
</html>