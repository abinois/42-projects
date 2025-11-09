#!/usr/bin/php
<?php
if ($argc != 2)
	echo "Incorrect Parameters\n";
else
{
	$string = preg_replace('/\s+/', "", trim($argv[1]));
	$tab = sscanf($string, "%d%c%d");
	if (count($tab) == 3 && is_numeric($tab[0]) && is_numeric($tab[2]))
	{
		if ($tab[1] == '+')
			echo ($tab[0] + $tab[2])."\n";
		else if ($tab[1] == '-')
			echo ($tab[0] - $tab[2])."\n";
		else if ($tab[1] == '*')
			echo ($tab[0] * $tab[2])."\n";
		else if ($tab[1] == '/')
			echo ($tab[0] / $tab[2])."\n";
		else if ($tab[1] == '%')
			echo ($tab[0] % $tab[2])."\n";
	}
	else
		echo "Syntax Error\n";
}
?>
