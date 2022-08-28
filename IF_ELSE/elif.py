a, b = int(input()), int(input())
if (a > b):
    print("NO")
elif (a < b):
    print("YES")
else:
    print("Don't know")

a, b, c = int(input()), int(input()), int(input())
if (a == b == c):
    print("Равносторонний")
elif (a == b or a == c or b == c):
    print("Равнобедренный")
else:
    print("Разносторонний")

a, b, c = int(input()), int(input()), int(input())
if (a <= b <= c):
    print(b)
elif (c <= b <= a):
    print(b)
elif (b <= a <= c):
    print(a)
elif (c <= a <= b):
    print(a)
else:
    print(c)

month = int(input())
if (month == 2):
    print(28)
elif (month == 4 or month == 6 or month == 9 or month == 11):
    print(30)
else:
    print(31)

weight = int(input())
if weight < 60:
    print("Легкий вес")
elif weight < 64:
    print("Первый полусредний вес")
else:
    print("Полусредний вес")

a, b, c = int(input()), int(input()), input()
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    if b == 0:
        print("На ноль делить нельзя!")
    else:
        print(a / b)
else:
    print("Неверная операция")

a, b = input(), input()
if ((a == "красный" or a == "синий" or a == "желтый") and (b == "красный" or b == "синий" or b == "желтый")):
    result = 0
    if (a == b):
        print(a)
    else:
        if (a == "красный" or b == "красный"):
            result += 1
        if (a == "синий" or b == "синий"):
            result += 2
        if (a == "желтый" or b == "желтый"):
            result += 3
        if (result == 3):
            print("фиолетовый")
        if (result == 4):
            print("оранжевый")
        if (result == 5):
            print("зеленый")
else:
    print("ошибка цвета")

x = int(input())
if x < 0 or x > 36:
    print("ошибка ввода")
else:
    if x == 0:
        print("зеленый")
    elif x <= 10:
        if x % 2:
            print("красный")
        else:
            print("черный")
    elif x <= 18:
        if x % 2:
            print("черный")
        else:
            print("красный")
    elif x <= 28:
        if x % 2:
            print("красный")
        else:
            print("черный")
    elif x <= 36:
        if x % 2:
            print("черный")
        else:
            print("красный")

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if b1 < a2 or b2 < a1:
    print("пустое множество")
elif b1 == a2:
    print(b1)
elif a1 == b2:
    print(a1)
elif a1 <= a2 < b1 < b2:
    print(a2, b1)
elif a2 <= a1 < b2 < b1:
    print(a1, b2)
elif a1 < a2 < b2 <= b1:
    print(a2, b2)
elif a2 < a1 < b1 <= b2:
    print(a1, b1)
elif a1 == a2 and b1 == b2:
    print(a1, b1)

a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())

print("Наименьшее число =", min(a, b, c, d, e))
print("Наибольшее число =", max(a, b, c, d, e))

a, b, c = int(input()), int(input()), int(input())
print(max(a, b, c))
print(a + b + c - min(a, b, c) - max(a, b, c))
print(min(a, b, c))

n = int(input())
a, b, c = n // 100, (n % 100) // 10, n % 10
if (max(a, b, c) - min(a, b, c) == a + b + c - max(a, b, c) - min(a, b, c)):
    print("Число интересное")
else:
    print("Число неинтересное")

a, b, c, d, e = float(input()), float(input()), float(input()), float(input()), float(input())
print(abs(a) + abs(b) + abs(c) + abs(d) + abs(e))

p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
print(abs(p1 - q1) + abs(p2 - q2))
