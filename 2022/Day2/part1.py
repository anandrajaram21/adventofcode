def win(a, b):
    a = a.lower()
    b = b.lower()
    if a == "a" and b == "y":
        return 6
    if a == "b" and b == "z":
        return 6
    if a == "c" and b == "x":
        return 6
    if a == "a" and b == "x":
        return 3
    if a == "b" and b == "y":
        return 3
    if a == "c" and b == "z":
        return 3
    return 0

def score(x):
    x = x.lower()
    if x == "x" or x == "a":
        return 1
    if x == "y" or x == "b":
        return 2
    if x == "z" or x == "c":
        return 3


with open("input.txt") as f:
    sum = 0
    contents = f.readlines()
    for i in contents:
        a, b = i.split()
        sum += win(a, b) + score(b)
    
    print(sum)