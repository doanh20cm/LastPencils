def enter(text):
    try:
        global pens
        print(text)
        pens = int(input())
        if pens < 1:
            enter("The number of pencils should be positive")
    except ValueError:
        enter("The number of pencils should be numeric")

def choose(text):
    global n
    print(text)
    n = input()
    if n not in ["Jack", "John"]:
        choose("Choose between 'John' and 'Jack'")

def take_check(text):
    try:
        global take
        global pens
        print(text)
        take = int(input())
        if take not in [1, 2, 3]:
            take_check("Possible values: '1', '2' or '3'")
        if take > pens:
            take_check("Too many pencils were taken")
    except ValueError:
        take_check("Possible values: '1', '2' or '3'")

def bot(bot_name):
    global take
    global pens
    print(bot_name + "'s turn!")
    if pens % 4 == 0:
        take = 3
    if pens % 4 == 3:
        take = 2
    if pens % 4 == 2:
        take = 1
    if pens % 4 == 1:
        take = 1
    print(take)

pens = 0
enter("How many pencils would you like to use:")
n = ""
choose("Who will be the first (John, Jack):")
if n == "John":
    count = 1
if n == "Jack":
    count = 0
while pens > 0:
    print("|" * pens)
    take = 0
    if count % 2 == 0:
        bot("Jack")
    else:
        take_check("John's turn!")
    pens -= take
    count += 1
print("Jack won!" if count % 2 == 0 else "John won!")