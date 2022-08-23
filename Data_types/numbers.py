a, b = float(input()), float(input())
print(0.5 * a * b)

s, v1, v2 = float(input()), float(input()), float(input())
v = v1 + v2
print(s / v)

f = float(input())
print(5 / 9 * (f - 32))

x = float(input())
if (x == 0):
    print("Обратного числа не существует")
else:
    print(1 / x)

n = int(input())
result = 0
for i in range(n):
    if (i < 2):
        result += 10.5
    else:
        result += 4
print(result)
