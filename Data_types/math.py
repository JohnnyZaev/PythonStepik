import math
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
print(math.dist((x1, y1), (x2, y2)))

import math
R = float(input())
print(math.pi * R ** 2, math.pi * 2 * R, sep='\n')

import math
a, b = float(input()), float(input())
print((a + b) / 2, math.sqrt(a * b), 2 * a * b / (a + b), math.sqrt((a ** 2 + b ** 2) / 2), sep = '\n')
