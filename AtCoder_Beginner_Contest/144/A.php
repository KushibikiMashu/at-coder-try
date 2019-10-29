<?php

$a = trim(fgets(STDIN));
$b = explode(' ', $a);

$ans = 1;
foreach ($b as $number) {
    if ($number >= 9) {
        $ans = -1;
        break;
    }
    $ans *= $number;
}

echo $ans;