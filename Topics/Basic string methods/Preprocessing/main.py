txt = input()
for t in txt:
    if t in [".", ",", "!", "?"]:
        txt = txt.replace(t, "")
txt = txt.lower()
print(txt)