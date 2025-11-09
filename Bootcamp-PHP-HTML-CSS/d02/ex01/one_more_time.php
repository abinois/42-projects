#!/usr/bin/php
<?php
function get_month($month)
{
if (preg_match("/[Jj]anvier/", $month))
	return (1);
elseif (preg_match("/[Ff][eé]vrier/u", $month))
	return (2);
elseif (preg_match("/[Mm]ars/", $month))
	return (3);
elseif (preg_match("/[Aa]vril/", $month))
	return (4);
elseif (preg_match("/[Mm]ai/", $month))
	return (5);
elseif (preg_match("/[Jj]uin/", $month))
	return (6);
elseif (preg_match("/[Jj]uillet/", $month))
	return (7);
elseif (preg_match("/[Aa]o[uû]t/u", $month))
	return (8);
elseif (preg_match("/[Ss]eptembre/", $month))
	return (9);
elseif (preg_match("/[Oo]ctobre/", $month))
	return (10);
elseif (preg_match("/[Nn]ovembre/", $month))
	return (11);
elseif (preg_match("/[Dd][eé]cembre/u", $month))
	return (12);
return(0);
}
if ($argc > 1)
{
	if (!(preg_match("/^([Ll]undi|[Mm]ardi|[Mm]ercredi|[Jj]eudi|[Vv]endredi|[Ss]amedi|[Dd]imanche) (0?[1-9]|[1-2][0-9]|3[0-1]) ([Jj]anvier|[Ff][eé]vrier|[Mm]ars|[Aa]vril|[Mm]ai|[Jj]uin|[Jj]uillet|[Aa]o[uû]t|[Oo]ctobre|(([Ss]ept|[Nn]ov|[Dd][eé]c)embre)) [0-9]{4} ([0-1][0-9]|2[0-4]):([0-5][0-9]|60):([0-5][0-9]|60)$/u", $argv[1])))
		echo "Wrong Format\n";
	else
	{
		$tab = explode(" ", $argv[1]);
		$time = explode(":", $tab[4]);
		$month = get_month($tab[2]);
		date_default_timezone_set('Europe/Paris');
		echo mktime($time[0], $time[1], $time[2], $month, $tab[1], $tab[3])."\n";
	}
}
?>
