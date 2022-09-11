for i in range(10):
    print("Python is awesome!")

a, b = input(), int(input())
for i in range(b):
    print(a)

for i in range(6):
    print("AAA")
for i in range(5):
    print("BBBB")
print("E")
for i in range(9):
    print("TTTTT")
print("G")

for i in range(int(input())):
    print("*" * 19)

name = input()
for i in range(10):
    print(i, name)

for i in range(int(input()) + 1):
    print("Квадрат числа", i, "равен", i ** 2)

w = int(input())
for i in range(w):
    print('*' * w)
    w -= 1

a, b = int(input()), int(input())
for i in range(int(input())):
    print(i + 1, a * (b / 100 + 1) ** i)
