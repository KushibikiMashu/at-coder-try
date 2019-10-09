<?php

$s = trim(fgets(STDIN));

$i = 0;
$no = false;
while (isset($s[$i])) {
    if ($i % 2 === 0 && $s[$i] === 'L' || $i % 2 === 1 && $s[$i] === 'R') {
        $no = true;
        break;
    }
    $i++;
}

echo $no ? 'No' : 'Yes';