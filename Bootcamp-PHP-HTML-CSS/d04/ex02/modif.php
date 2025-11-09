<?php
if ($_POST["submit"] != "OK" || !$_POST["login"] || !$_POST["newpw"] || !$_POST["oldpw"])
	exit ("ERROR\n");
if (file_exists("../private/passwd"))
{
	$data = unserialize(file_get_contents("../private/passwd"));
	print_r($data);
	foreach ($data as $index => $user)
		if ($index === $_POST["login"] && $user["login"] === $_POST["login"] && $user["passwd"] === hash(gost, $_POST["oldpw"]))
		{
			$data[$index]["passwd"] = hash(gost, $_POST["newpw"]);
			file_put_contents("../private/passwd", serialize($data));
			exit ("OK\n");
		}
}
exit ("ERROR\n");
?>
