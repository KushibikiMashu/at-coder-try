<?php

$input = trim(fgets(STDIN));
$z = explode(' ', $input);

$a = $z[0];
$b = $z[1];
$x = $z[2];

if ($x < $a * $a * $b / 2) {
    $c = $x / ($a * $b / 2);
    echo 90 - rad2deg(atan2($c, $b));
} else {
    $d = 2 * ($b - $x / ($a * $a));
    echo rad2deg(atan2($d, $a));
}
