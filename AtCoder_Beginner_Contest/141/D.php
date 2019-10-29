<?php

$a = explode(' ', trim(fgets(STDIN)));
$numbers = explode(' ', trim(fgets(STDIN)));

$n = $a[0];
$m = $a[1];

$heap = new SplMaxHeap();

foreach ($numbers as $n) {
    $heap->insert((int)$n);
}

for ($i = 0; $i < $m; $i++) {
    $max = floor($heap->extract() / 2);
    $heap->insert($max);
}

$ans = [];
while ($heap->valid()) {
    $ans[] = $heap->extract();
}

echo array_sum($ans);