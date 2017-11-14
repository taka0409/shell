#!/bin/bash
cd linux-4.14
echo ===== TEXT FILES ===== >> linus.log
grep -rl Linus --include='*.txt' >> linus.log
echo ===== C FILES ===== >> linus.log
grep -rl Linus --include='*.c' --include='*.h' >> linus.log
