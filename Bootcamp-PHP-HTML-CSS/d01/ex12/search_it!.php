#!/usr/bin/php
<?php
foreach ($argv as $index => $arg)
	if ($index > 1)
	{
		$val = explode(':', trim($arg));
		if ($val[0] == $argv[1])
			$lastval = $val[1];
	}
if ($lastval)
	echo "$lastval\n";
?>
