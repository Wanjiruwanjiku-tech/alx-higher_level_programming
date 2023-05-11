#!/usr/bin/python3
import calculator_1

a = 10
b = 5
sumation = calculator_1.add(a, b)
print("{} + {} = {}".format(a, b, sumation))
difference = calculator_1.sub(a, b)
print("{} - {} = {}".format(a, b, difference))
multi = calculator_1.mul(a, b)
print("{} * {} = {}".format(a, b, multi))
division = calculator_1.div(a, b)
print("{} / {} = {}".format(a, b, division))
