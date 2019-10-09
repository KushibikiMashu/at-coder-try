<?php

$a = trim(fgets(STDIN));
$b = trim(fgets(STDIN));

$c = explode(' ', $a);
$h = explode(' ', $b);

$n = $c[0];
$k = $c[1];

$count =0;
foreach ($h as $tall) {
    if((int)$tall >= (int)$k){
        $count += 1;
    }
}

echo $count;