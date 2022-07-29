text = input()
result = ""
for w in text:
    if w.isupper():
        result += "_" + w.lower()
    else:
        result += w
print(result)