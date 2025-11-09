<?php
Class Jaime
{
	Function sleepWith($princess)
	{
		if ($princess instanceof Sansa)
			echo "Let's do this.\n";
		elseif ($princess instanceof Cersei)
			echo "With pleasure, but only in a tower in Winterfell, then.\n";
		else
			echo "Not even if I'm drunk !\n";
	}
}
?>
