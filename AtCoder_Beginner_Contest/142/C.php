<?php

$n = trim(fgets(STDIN));
$m = trim(fgets(STDIN));
$ids = explode(' ', $m);

$ans = [];
foreach ($ids as $key => $id) {
    $ans[$id] = $key + 1;
}

ksort($ans);
echo implode(' ', $ans);
