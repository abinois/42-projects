#!/usr/bin/php
<?php
if(($source = file_get_contents($argv[1])) === FALSE)
	exit();
preg_match_all("/<img.+src\s*=\s*[\"\'](.*?)[\"\']/iu", $source, $matches);
$host = parse_url($argv[1], PHP_URL_HOST);
if (!file_exists($host))
	mkdir($host);
foreach ($matches[1] as $key => $match)
{
	if (!strstr($match, $argv[1]) && !strstr($match, "http"))
		$match = $match[0] != '/' ? $argv[1]."/".$match : $argv[1].$match;
	$file_name = strrchr($match, '/');
	if (file_exists($host.$file_name))
	{
		$ext = strrchr($file_name, '.');
		$file_name = str_ireplace("$ext", "($key)$ext", $file_name);
	}
	file_put_contents($host.$file_name, file_get_contents($match));
}
?>
