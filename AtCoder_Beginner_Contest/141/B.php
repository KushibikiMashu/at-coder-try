<?php

$s = trim(fgets(STDIN));

$i = 0;
$len = strlen($s);
$no = false;

for ($i = 0; $i < $len; $i++) {
    if ($i % 2 === 0 && $s[$i] === 'L' || $i % 2 === 1 && $s[$i] === 'R') {
        $no = true;
        break;
    }
}

echo $no ? 'No' : 'Yes';