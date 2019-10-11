<?php

$a = trim(fgets(STDIN));
$b = trim(fgets(STDIN));

for ($i = 0; $i < 3; $i++) {
    $c += $a[$i] === $b[$i] ? 1 : 0;
}

echo $c;