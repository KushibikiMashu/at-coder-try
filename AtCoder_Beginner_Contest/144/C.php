<?php

$a = (int)trim(fgets(STDIN));

$i = 0;
$pairs = [];
for ($i = 1; $i <= $a / 2; $i++) {
    if ($a % $i === 0) {
        $pairs[] = $a / $i + $i;
    }
    if ($a / $i <= $i) {
        break;
    }
}

echo min($pairs) - 2;
