<?php

$a = (int)trim(fgets(STDIN));

$ans = 'No';
for ($i = 1; $i < 10; $i++) {
    for ($j = 1; $j < 10; $j++) {
        if ($i * $j === $a) {
            $ans = 'Yes';
            break;
        }
    }
}

echo $ans;