def score(x):
    x = x.lower()
    if x == "x" or x == "a":
        return 1
    if x == "y" or x == "b":
        return 2
    if x == "z" or x == "c":
        return 3

def win(a, b):
    a = a.lower()
    b = b.lower()
    if a == "a":
        if b == "x":
            return 0 + score("c")
        elif b == "y":
            return 3 + score("a")
        elif b == "z":
            return 6 + score("b")
    if a == "b":
        if b == "x":
            return 0 + score("a")
        elif b == "y":
            return 3 + score("b")
        elif b == "z":
            return 6 + score("c")
    if a == "c":
        if b == "x":
            return 0 + score("b")
        elif b == "y":
            return 3 + score("c")
        elif b == "z":
            return 6 + score("a")
    return 0

with open("input.txt") as f:
    sum = 0
    contents = f.readlines()
    for i in contents:
        a, b = i.split()
        sum += win(a, b)
    
    print(sum)