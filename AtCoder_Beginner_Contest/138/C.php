<?php

$n = trim(fgets(STDIN));
$nums = explode(' ', trim(fgets(STDIN)));

sort($nums);
$sum = ($nums[0] + $nums[1]) / 2;

if ($n > 2) {
    for ($i = 2; $i < $n; $i++) {
        $sum = ($sum + $nums[$i]) / 2;
    }
}

echo $sum;