<?php
Class Color
{
	public $red, $green, $blue;
	static $verbose = FALSE;

	Function __construct($tab) {
		if (isset($tab['rgb']))
		{
			$val = intval($tab['rgb']);
			$this->red = ($val >> 16) & 0xff;
			$this->green = ($val >> 8) & 0xff;
			$this->blue = $val & 0xff;
			if (Self::$verbose)
				printf("Color( red: %3d, green: %3d, blue: %3d ) constructed.\n", $this->red, $this->green, $this->blue);
		}
		elseif (isset($tab['red']) && isset($tab['green']) && isset($tab['blue']))
		{
			$this->red = intval($tab['red']);
			$this->green = intval($tab['green']);
			$this->blue = intval($tab['blue']);
			if (Self::$verbose)
				printf("Color( red: %3d, green: %3d, blue: %3d ) constructed.\n", $this->red, $this->green, $this->blue);
		}
	}
	Function __destruct() {
		if (Self::$verbose)
			printf("Color( red: %3d, green: %3d, blue: %3d ) destructed.\n", $this->red, $this->green, $this->blue);
	}
	Function __toString() {
		return (sprintf("Color( red: %3d, green: %3d, blue: %3d )", $this->red, $this->green, $this->blue));
	}
	static Function doc() {
		return (file_get_contents("Color.doc.txt"));
	}
	Function add($toAdd) {
		return (new Self(array('red' => ($this->red + $toAdd->red), 'green' => ($this->green + $toAdd->green), 'blue' => ($this->blue + $toAdd->blue))));
	}
	Function sub($toSub) {
		return (new Self(array('red' => ($this->red - $toSub->red), 'green' => ($this->green - $toSub->green), 'blue' => ($this->blue - $toSub->blue))));
	}
	Function mult($factor) {
		return (new Self(array('red' => ($this->red * $factor), 'green' => ($this->green * $factor), 'blue' => ($this->blue * $factor))));
	}
}
?>
