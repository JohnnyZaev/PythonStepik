print('''"Python is a great language!", said Fred. "I don't ever remember having this much fun before."''')

name = input()
surname = input()
print("Hello", name, surname, end="! ")
print("You just delved into Python")

name = input()
print("Футбольная команда", name, "имеет длину", len(name), "символов")

town1, town2, town3 = input(), input(), input()
len1, len2, len3 = len(town1), len(town2), len(town3)
if (min(len1, len2, len3) == len1):
    print(town1)
elif (min(len1, len2, len3) == len2):
    print(town2)
else:
    print(town3)
if (max(len1, len2, len3) == len1):
    print(town1)
elif (max(len1, len2, len3) == len2):
    print(town2)
else:
    print(town3)

a, b, c = len(input()), len(input()), len(input())
if (2 * b - c - a) * (2 * c - b - a) * (2 * a - b - c) == 0:
    print("YES")
else:
    print("NO")

if 'синий' in input():
    print("YES")
else:
    print("NO")
