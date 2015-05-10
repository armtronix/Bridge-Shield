<?php
if($_REQUEST)
{
$num = $_REQUEST['num'];
if($num == 0){
    exec('sudo python3 /var/www/server/control.py ' . $num);
    echo "0";
    }
elseif ($num == 1){
     exec('sudo python3 /var/www/server/control.py ' . $num);
     echo "1";
    }
elseif ($num == 2){
     exec('sudo /usr/bin/python3 /var/www/server/control.py ' . $num);
     echo "2";
    }
elseif ($num == 3){
     exec('sudo /usr/bin/python3 /var/www/server/control.py ' . $num);
     echo "3";
    }
elseif ($num == 4){
     exec('sudo /usr/bin/python3 /var/www/server/control.py ' . $num);
     echo "4";
    }
elseif ($num == 5){
     exec('sudo /usr/bin/python3 /var/www/server/control.py ' . $num);
     echo "5";
    }
elseif ($num == 6){
     exec('sudo /usr/bin/python3 /var/www/server/control.py ' . $num);
     echo "6";
    }

else
     echo "can't dtermine state";
}
?>
