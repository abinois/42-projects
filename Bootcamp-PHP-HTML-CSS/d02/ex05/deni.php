#!/usr/bin/php
<?php
if ($argc != 3 || !file_exists($argv[1]))
	exit();
$bigtab = array();
$file = fopen($argv[1], 'r');
while ($line = fgetcsv($file, 0, ";"))
	$bigtab[] = $line;
if (($key_search = array_search($argv[2], $bigtab[0])) === FALSE)
	exit();
foreach ($bigtab[0] as $key => $column)
{
	$tmp = array();
	foreach ($bigtab as $index => $elem)
		if ($index)
			$tmp[$elem[$key_search]] = $elem[$key]; 
	$$column = $tmp;
}
while (1)
{
	echo "Entrez votre commande: ";
	$cmd = trim(fgets(STDIN));
	if (feof(STDIN))
		exit("\n");
	eval($cmd);
}
?>
