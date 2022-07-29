a = int(input())
count = 0
s = 0
while a != 55:
    count += 1
    s += a
    a = int(input())
print(count)
print(s)
print(round(s/count))
