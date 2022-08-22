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
