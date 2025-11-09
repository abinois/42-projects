#!/usr/bin/php
<?php
if ($argc != 4)
	echo "Incorrect Parameters\n";
else
{
	foreach ($argv as $arg)
		$op[] = preg_replace('/\s+/', " ", trim($arg));
	switch ($op[2])
	{
		case "+":
			echo ($op[1] + $op[3])."\n";
			break;
		case "-":
			echo ($op[1] - $op[3])."\n";
			break;
		case "/":
			echo ($op[1] / $op[3])."\n";
			break;
		case "*":
			echo ($op[1] * $op[3])."\n";
			break;
		case "%":
			echo ($op[1] % $op[3])."\n";
			break;
	}
}
?>
