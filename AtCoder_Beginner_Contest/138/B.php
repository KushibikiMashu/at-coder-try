<?php

$a = trim(fgets(STDIN));
$nums = explode(' ', trim(fgets(STDIN)));

$sum = 0;
foreach ($nums as $n) {
    $sum += 1 / $n;
}

echo 1 / $sum;
