<?php
require_once "../ex00/Color.class.php";
Class Vertex
{
	private $_x, $_y, $_z, $_w = 1.0;
	private $_color;

/* //////  I N F O  ////// */
	static $verbose = FALSE;
	static Function doc() { return (file_get_contents("Vertex.doc.txt")); }
	Function __toString()
	{
		if (Self::$verbose)
			return (sprintf("Vertex( x: %.2f, y: %.2f, z:%.2f, w:%.2f, Color( red: %3d, green: %3d, blue: %3d ) )",
			$this->_x, $this->_y, $this->_z, $this->_w, $this->_color->red, $this->_color->green, $this->_color->blue));
		else
			return (sprintf("Vertex( x: %.2f, y: %.2f, z:%.2f, w:%.2f )", $this->_x, $this->_y, $this->_z, $this->_w));
	}

/* //////  B U I L D  ////// */
	Function __construct($vertex)
	{
		if (isset($vertex['x']) && isset($vertex['y']) && isset($vertex['z']))
		{
			$this->_x = $vertex['x'];
			$this->_y = $vertex['y'];
			$this->_z = $vertex['z'];
			if (isset($vertex['w']))
				$this->_w = $vertex['w'];
			$this->_color = (isset($vertex['color']) && $vertex['color'] instanceof Color) ? $vertex['color'] : new Color(array('rgb' => 16777215));
			if (Self::$verbose)
                printf("Vertex( x: %.2f, y: %.2f, z:%.2f, w:%.2f, Color( red: %3d, green: %3d, blue: %3d ) ) constructed\n",
					$this->_x, $this->_y, $this->_z, $this->_w, $this->_color->red, $this->_color->green, $this->_color->blue);
		}
	}
	Function __destruct() {
		if (Self::$verbose)
			printf("Vertex( x: %.2f, y: %.2f, z:%.2f, w:%.2f, Color( red: %3d, green: %3d, blue: %3d ) ) destructed\n",
				$this->_x, $this->_y, $this->_z, $this->_w, $this->_color->red, $this->_color->green, $this->_color->blue);
	}

/* //////  Accessing  Functions  ////// */
	Function x_of() { return $this->_x; }
	Function y_of() { return $this->_y; }
	Function z_of() { return $this->_z; }
	Function w_of() { return $this->_w; }
	Function color_of() { return $this->_color; }

/* //////  Setting  Functions  ////// */
	Function setX($val) { $this->_x = $val; }
	Function setY($val) { $this->_y = $val; }
	Function setZ($val) { $this->_z = $val; }
	Function setW($val) { $this->_w = $val; }
	Function setColor($val) { $this->_color = $val; }
}
?>
