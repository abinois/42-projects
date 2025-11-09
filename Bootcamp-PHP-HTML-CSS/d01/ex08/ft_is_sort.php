<?php
function ft_is_sort($tab)
{
	$len = count($tab);
	$old = $tab;
	sort($tab);
	while (--$len >= 0)
		if ($old[$len] != $tab[$len])
			return (FALSE);
	return (TRUE);
}
?>
