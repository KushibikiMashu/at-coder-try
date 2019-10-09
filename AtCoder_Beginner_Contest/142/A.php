<?php

$n = (int)trim(fgets(STDIN));
echo $n % 2 === 0 ? 0.5 : ($n + 1) / (2 * $n);