<?php

$a = trim(fgets(STDIN));
$b = explode(' ', $a);

$n = $b[0];
$k = $b[1];
$q = $b[2];

$arr = array_fill(1, $q, -(int)$k + 2);
$scores = $arr;
while ($index = fgets(STDIN)) {
    $scores[$index] += 1;
}

foreach ($arr as $key => $val) {
    echo ($val + $scores[$key]) > 0 ? 'Yes' : 'No';
}
