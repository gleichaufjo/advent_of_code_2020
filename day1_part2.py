import numpy as np
from numpy import loadtxt
lines = loadtxt("input_day1.txt", comments="#", delimiter=" ", unpack=False)
print(lines)


for j in lines:
   for i in lines:
    for k in lines:
       x = i + j + k
       if x == 2020:
            n = i
            m = j
            p = k
            result = n * m * p
            print(result)
