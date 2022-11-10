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
    <h1 style=
<?php
    $directory = 'C:\xampp\htdocs\static';

    if (!is_dir($directory)) {
        exit('Invalid diretory path');
    }

    $files = array();
    foreach (scandir($directory) as $file) {
        if ($file !== '.' && $file !== '..') {
            $files[] = $file;
        }
    }
    $a=count($files);
    //echo $a;
    $c=0;
    $sym = $_GET['keyword'];
   // echo $sym;
    foreach($files as $fil){
        $file=basename($fil,".py");
        $c=$c+1;
        if($sym==$file)
        {
            //echo 'success';
            $command_exec = escapeshellcmd("python3 $file.py");
            $str_output = shell_exec($command_exec);
            echo '<span style="color: #696969;font-size: 10px;font-weight: 300;line-height: 22px;padding: 10px;">'.$str_output.'</span>';
            
           exit;
          
        }
        if($c==$a)
        {
   $output = shell_exec("python3 qwe.py $sym");
   echo '<color: #696969;font-size: 10px;font-weight: 300;line-height: 22px;padding: 10px;">'.$output.'</span>';
        }
   
       
    }

   // var_dump($files);
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