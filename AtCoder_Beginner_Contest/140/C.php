<?php

$n = trim(fgets(STDIN));
$nums = explode(' ', trim(fgets(STDIN)));

$ans = $nums[0];
$count = count($nums);

for ($i = 0; $i < $count - 1; $i++) {
    if ($nums[$i] <= $nums[$i + 1]) {
        $ans += $nums[$i];
    } else {
        $ans += $nums[$i + 1];
    }
}
$ans += $nums[$count - 1];

echo $ans;