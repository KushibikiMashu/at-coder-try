<?php

$n = trim(fgets(STDIN));
$nums = explode(' ', trim(fgets(STDIN)));

$count = 0;
$max = 0;
for ($i = 0; $i < $n - 1; $i++) {
    $cur = $nums[$i];
    $next = $nums[$i + 1];

    if ($cur >= $next) {
        $count++;
    } else {
        if ($max < $count) {
            $max = $count;
        }
        $count = 0;
    }
}

echo $max > $count ? $max : $count;
