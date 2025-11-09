<?php
function ft_split($str)
{
	$tab = explode(" ", preg_replace('/\s+/', " ", trim($str)));
	sort($tab);
	return($tab);
}
?>
