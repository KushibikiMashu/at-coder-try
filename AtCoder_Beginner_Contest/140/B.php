<?php

$n = trim(fgets(STDIN));
$a = explode(' ', trim(fgets(STDIN)));
$b = explode(' ', trim(fgets(STDIN)));
$c = explode(' ', trim(fgets(STDIN)));

$sum = array_sum($b);
for ($i = 0; $i < $n - 1; $i++) {
    if ($a[$i] + 1 === (int)$a[$i + 1]) {
        $sum += $c[$a[$i] - 1];
    }
}

echo $sum;