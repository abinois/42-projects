#!/usr/bin/php
<?php
$fd = fopen("/var/run/utmpx", "r");
date_default_timezone_set("Europe/Paris");
while (($str = fread($fd, 628)))
{
	$tab = unpack("a256user/a4id/a32line/ipid/itype/I2time/a256host/i16pad", $str);
	if ($tab[type] == "7")
	{
		$date = date("M j H:i", $tab[time1]);
		echo $tab[user]."  ".$tab[line]."  ".$date."\n";
	}
}
?>
