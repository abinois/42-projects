<?php
session_start();
include "auth.php";
if ($_GET["login"] && $_GET["passwd"] && auth($_GET["login"], $_GET["passwd"]))
{
	$_SESSION["loggued_on_user"] = $_GET["login"];
	exit ("OK\n");
}
$_SESSION["loggued_on_user"] = "";
exit ("ERROR\n");
?>
