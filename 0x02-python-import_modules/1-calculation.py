#!/usr/bin/python3
import calculator_1 as cal
a = 10
b = 5
addition = cal.add(a, b)
subtract = cal.sub(a, b)
divide = int(cal.div(a, b))
multiple = cal.mul(a, b)
print("{:d} + {:d} = {:d}".format(a, b, addition))
print("{:d} - {:d} = {:d}".format(a, b, subtract))
print("{:d} * {:d} = {:d}".format(a, b, multiple))
print("{:d} / {:d} = {:d}".format(a, b, divide))
