#!/usr/bin/sh
url="https://adventofcode.com/2021/day/$1/input"
cookie=$(cat cookie)
curl $url -o data/$1.in --cookie "session=$cookie"
head data/$1.in
