#!/bin/bash
for ((i=1;i<=500;i++));
do
    $echo ./unknown ${i} >> unknown.log
done
