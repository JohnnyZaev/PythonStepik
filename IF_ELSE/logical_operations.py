if (-1 < int(input()) < 17):
    print("Принадлежит")
else:
    print("Не принадлежит")

n = int(input())
if (n <= -3 or n >= 7):
    print("Принадлежит")
else:
    print("Не принадлежит")

x = int(input())
if (-30 < x <= -2 or 7 < x <= 25):
    print("Принадлежит")
else:
    print("Не принадлежит")

n = int(input())
if (999 < n < 10000) and (n % 7 == 0 or n % 17 == 0):
    print("YES")
else:
    print("NO")

a, b, c = int(input()), int(input()), int(input())
if (a < b + c and b < c + a and c < a + b):
    print("YES")
else:
    print("NO")

year = int(input())
if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    print("YES")
else:
    print("NO")
