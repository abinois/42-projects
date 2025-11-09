<?php
$fd = fopen("list.csv", 'r');
if ($fd != FALSE)
{
    $valors = array();
    $bigtab = array();
    while (($line = fgetcsv($fd, 0, ";")))
        $bigtab[] = $line;
    $index = 0;
    if (!empty($bigtab))
    {
        foreach ($bigtab as $key => $line)
        {
            $line[0] = $index++;
            $valors[] = $line[1];
            $bigtab[$key] = implode(";", $line);
        }
        file_put_contents("bigtab.txt", $bigtab);
        file_put_contents("list.csv", implode(PHP_EOL, $bigtab).PHP_EOL);
        echo json_encode($valors);
    }
    fclose($fd);
}
?>