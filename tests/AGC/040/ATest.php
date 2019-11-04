<?php

use PHPUnit\Framework\TestCase;

class AGC040 extends TestCase
{
    /**
     * @dataProvider Adata
     *
     * @param $a
     * @param $b
     */
    public function testA($a, $b)
    {
        $result = $this->solveA($a);
        $this->assertSame($b, $result);
    }

    /**
     * @return array
     */
    public function Adata()
    {
        return [
            ['<>>', 3],
            ['<>>><<><<<<<>>><', 28],
        ];
    }

    /**
     * @param $a
     * @return int
     */
    private function solveA($a)
    {
        $arr = str_split($a);
        $count = count($arr);
        $ans = array_fill(0, $count + 1, 0);

        $j = 1;
        foreach ($arr as $k => $v) {
            if ($v === '<') {
                $ans[$k + 1] = $j;
                $j += 1;
            } else {
                $j = 1;
            }
        }

        $j = 1;
        foreach (array_reverse($arr) as $k => $v) {
            if ($v === '>') {
                $ans[$k] = max($ans[$k], $j);
                $j += 1;
            } else {
                $j = 1;
            }
        }
        var_dump($ans);

        return array_sum($ans);
    }
}