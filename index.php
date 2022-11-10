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
        <section class="header">
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
            
<div class="text-box">
            <h1>Price Comparision</h1>
            <p>Price Comparision Site use to compare prices between the Products <br></p>
            <br>
            <form action="trav.php" method = "get" >
            <label for="name" class="hero-btn">Enter the product to be searched
          <input type="text" name="keyword"></label>
          <input type="Submit" value="submit" class="hero-btn"></form>
            </div>
        </section>
<!--------------Features-------------->
<section class="course">
        <h1> Our Speciality </h1>
    <br>
        <br>
    <h>Our systems performs several important functions that guarantee the integrity and consistency of the data in our database. We use some cutting edge technoloies to safely secure and store data. Here are the some of our specialities. </h>
    <div class="row">
        <div class="course-col">
    <h3> Money Saving</h3>
        <p>You can easily and quickly find the best deal, and save yourself a good amount of money </p>
    </div>
        <div class="course-col">
    <h3> Convenient </h3>
        <p> You can take a fraction of the time it would otherwise take to find all the results and receive all of the information on one screen at one time.</p>
    </div>
        <div class="course-col">
    <h3> Wide Choice </h3>
        <p>You can choose any website from the multiple results given.</p>
    </div>
</div>
</section>
<section class="footer">
<h4>About Us</h4> 
    <p> Check out our social media profiles.<br></p>
    <div class="icons">
        <a href="https://www.instagram.com/zephyr._7/"><i class="fa fa-instagram"></i></a>
        <a href="https://www.linkedin.com/in/manvith-devadiga-667967178/"><i class="fa fa-linkedin"></i></a>
        <a href="https://twitter.com/z_e_p_y_r_"><i class="fa fa-twitter"></i></a>
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