<?php
if ($_GET["action"] != NULL && $_GET["name"] != NULL && $_GET["name"] != "")
{
	if ($_GET["action"] === "set" && $_GET["value"] != NULL && $_GET["value"] != "")
		setcookie($_GET["name"], $_GET["value"], time() + (24 * 60 * 60));
	elseif ($_GET["action"] === "get" && $_COOKIE[$_GET["name"]] != NULL)
		echo $_COOKIE[$_GET["name"]]."\n";
	elseif ($_GET["action"] === "del" && $_COOKIE[$_GET["name"]] != NULL)
		setcookie($_GET["name"], NULL, time() - 1000);
}
?>
