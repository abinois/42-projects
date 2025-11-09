#!/usr/bin/php
<?php
$bigtab = array();
while (($line = fgetcsv(STDIN, 0, ";")))
	$bigtab[] = $line;
if ($argv[1] == "moyenne")
{
	$note = 0;
	$total = 0;
	foreach ($bigtab as $line)
		if ($line[2] != "moulinette" && is_numeric($line[1]))
		{
			$note++;
			$total += $line[1];
		}
	if ($note)
		echo ($total / $note)."\n";
}
elseif ($argv[1] == "moyenne_user" || $argv[1] == "ecart_moulinette")
{
	$users = array();
	foreach ($bigtab as $line)
		if (!empty($line[0]) && $line[2] != "moulinette" && is_numeric($line[1]))
		{
			$users[$line[0]]['note_number'] += 1;
			$users[$line[0]]['total'] += $line[1];
		}
		else if (!empty($line[0]) && $line[2] == "moulinette" && is_numeric($line[1]))
			$users[$line[0]]['moulinote'] = $line[1];
	ksort($users);
	if ($argv[1] == "moyenne_user")
	{
		foreach ($users as $key => $usr)
			if ($usr['note_number'])
				echo $key.":".($usr['total'] / $usr['note_number'])."\n";
	}
	elseif ($argv[1] == "ecart_moulinette")
		foreach ($users as $key => $usr)
			if ($usr['note_number'])
				echo $key.":".(($usr['total'] / $usr['note_number']) - $usr['moulinote'])."\n";
}
?>
