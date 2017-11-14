#!/bin/bash
data=($(ls -S))
for((i=0;i<3;i++));
do
    echo ${data[${i}]}
done
