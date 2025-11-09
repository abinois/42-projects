<?php
session_start();
if ($_SESSION['loggued_on_user'] != NULL && $_SESSION['loggued_on_user'] != "")
	exit ($_SESSION["loggued_on_user"]."\n");
else
	exit ("ERROR\n");
?>
