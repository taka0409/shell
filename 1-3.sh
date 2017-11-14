#!/bin/bash
min=$(./unknown 1)
minid=1
max=${min}
maxid=${minid}
for ((i=2;i<=500;i++)); 
do
    value=$(./unknown ${i})
    if [ ${value} -lt ${min} ]; then
        min=${value}
        minid=${i}
    elif [ ${value} -gt ${max} ]; then
        max=${value}
        maxid=${i}
    fi
done
echo ${min} ${minid}
echo ${max} ${maxid}
