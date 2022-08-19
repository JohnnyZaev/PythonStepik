a = int(input())
print(a, a + 1, a + 2, sep="\n")

print(int(input()) + int(input()) + int(input()))

a = int(input())
print("Объем =", a * a * a)
print("Площадь полной поверхности =", a * a * 6)

a, b = int(input()), int(input())
print(3 * (a + b)**3 + 275 * b**2 - 127 * a - 41)

a = int(input())
print("Следующее за числом", a, "число:", a + 1)
print("Для числа", a, "предыдущее число:", a - 1)

a, b, c, d = int(input()), int(input()), int(input()), int(input())
print((a + b + c + d) * 3)

a, b = int(input()), int(input())
print(a, "+", b, "=", a + b)
print(a, "-", b, "=", a - b)
print(a, "*", b, "=", a * b)

a, d, n = int(input()), int(input()), int(input())
print(a + d * (n - 1))

a = int(input())
print(a, a * 2, a * 3, a * 4, a * 5, sep="---")
