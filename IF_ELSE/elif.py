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
