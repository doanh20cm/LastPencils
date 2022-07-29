count = 0
t = 0
while True:
    num = input()
    if num == ".":
        break
    else:
        t += int(num)
        count += 1
print(t / count)