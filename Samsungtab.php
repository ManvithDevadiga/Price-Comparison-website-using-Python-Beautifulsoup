<!DOCTYPE html>
<html>
<head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Price Comparision</title>
        <link rel="stylesheet" href="style.css">
        <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@300;400&family=Ubuntu&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
        
    </head>
    <body>
        <section class="infoq">
            <nav>
                <a href="index.php"><img src="img/Logo_files/logo006.png"> </a>
                <center><img src="img/Logo_files/cname2.png" alt="Paris" class="center"></center>
                <div class="nav-links" id="navlinks">
                   <i class="fa fa-window-close-o" onclick="hidemenu()"></i>
                    <ul>
                    <li><a href="index.php">HOME</a></li>
                    <li><a href="Info.php">INFO</a></li>
                    <li><a href="about.php">ABOUT US</a></li>
                    </ul>
                </div>
                <i class="fa fa-bars" onclick="showmenu()"></i>
            </nav>
<h1>Price Details</h1>
            <p>Welcome To The World Of Products</p>

<!--------------Info-------------->
<div class="query">
<<?php
  $command_exec = escapeshellcmd("python3 Samsungtab.py");
  $str_output = shell_exec($command_exec);
 echo  $str_output;

?> 
</div>
<!-----------Comment Box-------->
            
<!--<div class="comment-box">
    <h3>Leave Comment</h3>
    <form class="comment-form">
        <input type="text" placeholder="Enter Name">
        <input type="email" placeholder="Enter Email">
        <textarea rows="5" placeholder="Your Comment"></textarea>
        <button type="submit" class="hero-btn red-btn">POST COMMENT</button>
    </form>      
</div>  --->       
</section>       
<!---------Footer----->        
        
<section class="footer">
<h4>About Us</h4> 
    <p> Check out our social media profiles.<br></p>
    <div class="icons">
     <a href="https://www.instagram.com"><i class="fa fa-instagram"></i></a>
        <a href="https://www.linkedin.com"><i class="fa fa-linkedin"></i></a>
        <a href="https://twitter.com"><i class="fa fa-twitter"></i></a>
    <i class="fa fa-i-cursor"></i>
    <i class="fa fa-instagram"></i>
    <i class="fa fa-linkedin"></i>
    <i class="fa fa-twitter"></i>
    
    </div>
    <p>Made with <i class="fa fa-heart-o"></i> 20IS410 and 20IS411</p>
</section>
        
<!--------------------Java Script------------>
        
     <script> 
        var navlinks = document.getElementById("navlinks")
        function showmenu(){
            navlinks.style.right = "0";
        }
        function hidemenu(){
            navlinks.style.right = "-200px";
        }
    </script>   
    </body>
</html>