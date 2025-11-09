<?php
abstract Class House
{
	abstract Function getHouseName();
	abstract Function getHouseSeat();
	abstract Function getHouseMotto();
	Function introduce()
	{
		printf("House %s of %s : \"%s\"\n", $this->getHouseName(), $this->getHouseSeat(), $this->getHouseMotto());
	}
}
?>
