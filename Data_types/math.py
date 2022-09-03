import math
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
print(math.dist((x1, y1), (x2, y2)))

import math
R = float(input())
print(math.pi * R ** 2, math.pi * 2 * R, sep='\n')
