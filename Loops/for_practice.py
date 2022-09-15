counter = 0
for i in range(int(input()), int(input()) + 1):
    if (i ** 3 % 10 == 4 or i ** 3 % 10 == 9):
        counter += 1
print(counter)

result = 0
for i in range(int(input())):
    result += int(input())
print(result)

n = int(input())
result = 0
for i in range(1, n + 1):
    temp = i ** 2
    if (temp % 10 == 2 or temp % 10 == 5 or temp % 10 == 8):
        result += i
print(result)
