#!/bin/bash

if [ $# -ne 1 ]; then
  echo "指定された引数は$#個です。" 1>&2
  echo "実行するには1個の引数が必要です。" 1>&2
  exit 1
fi

NUMBER=$1

mkdir "$NUMBER"

for i in A B C
do
  cp template.py "$NUMBER/$i.py"
done
