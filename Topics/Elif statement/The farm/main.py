a = int(input())
if a >= 23:
    if a >= 6769:
        print(str(a // 6769) + " sheep")
    elif a >= 3848:
        print("1 cow" if a // 3848 == 1 else str(a // 3848) + " cows")
    elif a >= 1296:
        print("1 pig" if a // 1296 == 1 else str(a // 1296) + " pigs")
    elif a >= 678:
        print("1 goat" if a // 678 == 1 else str(a // 678) + " goats")
    elif a >= 23:
        print("1 chicken" if a // 23 == 1 else str(a // 23) + " chickens")
else:
    print("None")