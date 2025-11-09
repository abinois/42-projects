<?php
abstract Class Fighter
{
	public $name;
	Function __construct($new_fighter) {
		$this->name = $new_fighter;
	}
	abstract Function fight($target);
}
?>
