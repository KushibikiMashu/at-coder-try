<?php

// 不正解
$a = explode(' ', trim(fgets(STDIN)));

$c = $a[0];
$n = $a[1];

$ans = 1;
$sum = (int)$c;
while ($sum < $n) {
    $sum += $c - 1;
    $ans++;
}

echo $ans;
