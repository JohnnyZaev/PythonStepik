b, q, n = int(input()), int(input()), int(input())
print(b * q ** (n - 1))

print(int(input()) // 100)

a, b = int(input()), int(input())
print(b // a, b % a, sep="\n")

a = int(input())
print(a // 2 + a % 2)

num = int(input())
a = num % 10
b = (num % 100) // 10
c = num // 100
print("Сумма цифр =", a + b + c)
print("Произведение цифр =", a * b * c)

num = int(input())
a = num % 10
b = (num % 100) // 10
c = (num % 1000) // 100
d = num // 1000
print("Цифра в позиции тысяч равна", d)
print("Цифра в позиции сотен равна", c)
print("Цифра в позиции десятков равна", b)
print("Цифра в позиции единиц равна", a)

num = int(input())
c = num % 10
b = (num % 100) // 10
a = num // 100
print(a, b, c, sep="")
print(a, c, b, sep="")
print(b, a, c, sep="")
print(b, c, a, sep="")
print(c, a, b, sep="")
print(c, b, a, sep="")
