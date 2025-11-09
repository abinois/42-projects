<?php
Class NightsWatch
{
	private $staff = array();
	Function recruit($new_staff)
	{
		$this->staff[] = $new_staff;
	}
	Function fight()
	{
		foreach ($this->staff as $people)
			if (method_exists(get_class($people), "fight"))
				$people->fight();
	}
}
?>
