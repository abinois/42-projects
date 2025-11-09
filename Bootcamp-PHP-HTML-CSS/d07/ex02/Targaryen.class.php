<?php
class Targaryen
{
	Function resistsFire() {
		return (FALSE);
	}
	Function getBurned() {
		return ($this->resistsFire() ? "emerges naked but unharmed" : "burns alive");
	}
}
?>
