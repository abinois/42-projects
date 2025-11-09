#!/usr/bin/php
<?php
function make_up($tab)
{
	$str = $tab[1].strtoupper($tab[2]).$tab[3];
	return ($str);
}
function match_a($tab)
{
	$str = preg_replace_callback("/(title\s*=\s*[\'\"])(.+?)([\'\"])/ui", "make_up", $tab[1]);
	$str = preg_replace_callback("/(>)(.+?)(<)/ui", "make_up", $str);
	return ($str);
}
if ($argc > 1)
{
	$file = file_get_contents($argv[1]);
	$new = preg_replace_callback("/(<a.*>.*< *\/a>)/sui", "match_a", $file);
	echo $new;
}
?>
