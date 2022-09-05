import math
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
print(math.dist((x1, y1), (x2, y2)))

R = float(input())
print(math.pi * R ** 2, math.pi * 2 * R, sep='\n')

a, b = float(input()), float(input())
print((a + b) / 2, math.sqrt(a * b), 2 * a * b / (a + b), math.sqrt((a ** 2 + b ** 2) / 2), sep = '\n')

x = float(input())
print(math.sin(math.radians(x)) + math.cos(math.radians(x)) + math.tan(math.radians(x)) ** 2)

x = float(input())
print(math.ceil(x) + math.floor(x))

a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
if d < 0:
    print("Нет корней")
elif d == 0:
    print(-b / (2 * a))
else:
    x1, x2 = (-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)
    print(min(x1, x2), max(x1, x2), sep='\n')

n, a = int(input()), float(input())
print((n * a ** 2) / (4 * math.tan(math.pi / n)))
