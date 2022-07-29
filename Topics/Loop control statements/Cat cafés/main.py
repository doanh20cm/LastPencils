l = []
while True:
    text = input()
    if text == "MEOW":
        break
    else:
        l.append(text.split())
l.sort(key=lambda cafe: cafe[1])
l.reverse()
print(l[0])
