#!/usr/bin/php
<?php
if($argc > 1)
{
	$phrase = preg_replace('/[ \t]+/', " ", trim($argv[1]));
	if (strlen($phrase))
		echo "$phrase\n";
}
?>
