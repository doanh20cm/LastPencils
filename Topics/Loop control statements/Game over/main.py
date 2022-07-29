scores = input().split()
count = 0
count_c = 0
for ans in scores:
    if ans == 'I':
        count += 1
        if count == 3:
            print("Game over")
            print(count_c)
            break
    else:
        count_c += 1
if count < 3:
    print("You won")
    print(count_c)