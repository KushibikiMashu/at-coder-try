<?php

$s = trim(fgets(STDIN));
$a = [
    'Sunny' => 'Cloudy',
    'Cloudy' => 'Rainy',
    'Rainy' => 'Sunny',
];

echo $a[$s];
