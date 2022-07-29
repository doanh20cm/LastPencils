a = float(input())
b = float(input())
opration = input()
if opration == "+":
    print(a + b)
if opration == "-":
    print(a - b)
if opration == "pow":
    print(a ** b)
if opration == "*":
    print(a * b)
if opration in {"/", "mod", "div"}:
    if b == 0:
        print("Division by 0!")
    else:
        if opration == "/":
            print(a / b)
        if opration == "mod":
            print(a % b)
        if opration == "div":
            print(a // b)