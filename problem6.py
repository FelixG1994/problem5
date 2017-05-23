#!/usr/bin/env python

i = 1
sum_of_squares = 0
squaresum = 0
while i <= 100:
    sum_of_squares = sum_of_squares + i**2
    squaresum = squaresum + i
    difference = squaresum**2 - sum_of_squares
    i+=1
print difference
