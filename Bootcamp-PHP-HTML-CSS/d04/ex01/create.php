<?php
if (!$_POST['login'] || !$_POST['passwd'] || $_POST['passwd'] == "" || $_POST['login'] == "" || $_POST['submit'] != "OK")
	exit ("ERROR\n");
if (file_exists("../private/passwd"))
{
	$data = unserialize(file_get_contents("../private/passwd"));
	foreach ($data as $key => $user)
		if ($key == $_POST['login'])
			exit ("ERROR\n");
	$tab['login'] = $_POST["login"];
	$tab['passwd'] = hash(gost, $_POST['passwd']);
	$data[$_POST['login']] = $tab;
	file_put_contents("../private/passwd", serialize($data));
}
else
{
	if (!file_exists("../private"))
		mkdir("../private");
	$tab['login'] = $_POST['login'];
	$tab['passwd'] = hash(gost, $_POST['passwd']);
	$data[$_POST['login']] = $tab;
	file_put_contents("../private/passwd", serialize($data));
}
exit ("OK\n");
?>
