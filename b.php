<?php
  //$keyword = 'iphone';
   //$command_exec = escapeshellcmd("python3 qwe.py .$keyword");
   //$str_output = shell_exec($command_exec);
   //echo $keyword;
   $sym = $_GET['keyword'];
   echo shell_exec("python3 qwe.py .$sym");
  //$output = exec("python qwe.py $keyword");
   //echo $output;

?>
