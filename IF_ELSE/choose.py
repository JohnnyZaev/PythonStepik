if (input() == input()):
    print("Пароль принят")
else:
    print("Пароль не принят")

if (int(input()) % 2):
    print("Нечетное")
else:
    print("Четное")

n = int(input())
if ((n % 10000) // 1000 + n % 10 == (n % 1000) // 100 - (n % 100) // 10):
    print("ДА")
else:
    print("НЕТ")

if (int(input()) < 18):
    print("Доступ запрещен")
else:
    print("Доступ разрешен")

a, b, c = int(input()), int(input()), int(input())
if ((b - a) + b == c):
    print("YES")
else:
    print("NO")

a, b = int(input()), int(input())
if (a < b):
    print(a)
else:
    print(b)

a, b, c, d = int(input()), int(input()), int(input()), int(input())
ab = 0
cd = 0
if (a < b):
    ab = a
else:
    ab = b
if (c < d):
    cd = c
else:
    cd = d
if (ab < cd):
    print(ab)
else:
    print(cd)

n = int(input())
if (n < 14):
    print("детство")
elif (n < 25):
    print("молодость")
elif (n < 60):
    print("зрелость")
else:
    print("старость")

result = 0
for i in range(3):
    a = int(input())
    if (a > 0):
        result += a
print(result)
