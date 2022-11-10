<html> 
	<head>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
	</head>
	<body>
        <form action = "ip1264.php">
          <center><input class="file_submit" type="Submit"></center>
        </form>
        <br>
        <br>
        <br>
    </body>

</html>
<?php
  $command_exec = escapeshellcmd("python3 ip1264.py");
  $str_output = shell_exec($command_exec);
 echo  $str_output;

?>