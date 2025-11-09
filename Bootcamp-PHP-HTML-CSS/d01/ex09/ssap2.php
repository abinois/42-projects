#!/usr/bin/php
<?php
function ft_split($str)
{
	$tab = explode(" ", preg_replace('/\s+/', " ", trim($str)));
	return($tab);
}
function special_strcmp($str1, $str2)
{
	$i = -1;
	$len1 = strlen($str1);
	$len2 = strlen($str2);
	$len = $len1 < $len2 ? $len1 : $len2;
	$str1 = strtolower($str1);
	$str2 = strtolower($str2);
	$base = "abcdefghijklmnopqrstuvwxyz0123456789";
	while (++$i < $len)
	{
		if (strpos($base, $str1[$i]) === FALSE && strpos($base, $str2[$i]) === FALSE && $str1[$i] > $str2[$i])
			return (TRUE);
		if (strpos($base, $str1[$i]) === FALSE)
			return (TRUE);
		if (strpos($base, $str2[$i]) === FALSE)
			return (FALSE);
		if (strpos($base, $str1[$i]) - strpos($base, $str2[$i]) > 0)
			return (TRUE);
	}
	return ($len == $len2 ? TRUE : FALSE);
}
function custom_sort($tab)
{
	$i = -1;
	$len = count($tab);
	while (++$i < $len - 1)
	{
		$j = 0;
		while ($i + ++$j < $len)
			if (special_strcmp($tab[$i], $tab[$i + $j]))
			{
				$tmp = $tab[$i];
				$tab[$i] = $tab[$i + $j];
				$tab[$i + $j] = $tmp;
			}
	}
	return ($tab);
}
$bigtab = array("alpha" => array(), "begin_alpha" => array(), "num" => array(), "begin_num"  => array(), "other" => array());
foreach ($argv as $index => $tab)
	if ($index)
	{
		$minitab = ft_split($tab);
		foreach ($minitab as $arg)
		{
			if (is_numeric($arg))
				array_push($bigtab["num"], $arg);
			elseif (is_numeric($arg[0]))
				array_push($bigtab["begin_num"], $arg);
			elseif (ctype_alpha($arg))
				array_push($bigtab["alpha"], $arg);
			elseif (ctype_alpha($arg[0]))
				array_push($bigtab["begin_alpha"], $arg);
			else
				array_push($bigtab["other"], $arg);
		}
	}
foreach ($bigtab as $key => $tab)
{
	if ($key === "alpha")
		sort($tab, SORT_STRING | SORT_FLAG_CASE);
	elseif ($key === "num")
		sort($tab);
	else
		$tab = custom_sort($tab);
	if (!empty($tab))
		foreach ($tab as $arg)
			echo "$arg\n";
}
?>
