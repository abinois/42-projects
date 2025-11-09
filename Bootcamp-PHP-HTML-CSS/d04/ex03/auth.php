<?php
function auth($login, $passwd)
{
    if (($table = unserialize(file_get_contents("../private/passwd"))) === FALSE)
		return (FALSE);
    foreach ($table as $user)
        if ($user["login"] === $login && $user["passwd"] === hash(gost, $passwd))
            return (TRUE);
    return (FALSE);
}
?>
