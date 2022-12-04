def findcommon(a, b, c):
    for i in a:
        for j in b:
            for k in c:
                if i == j and j == k:
                    return i

def wordscore(a):
    if a.islower():
        return ord(a) - 96
    else:
        return ord(a) - 38

with open("input.txt") as f:
    rucksacks = f.readlines()
    rucksacks = [i.strip() for i in rucksacks]
    sum = 0
    # Make a list of every three lines in rucksacks
    rucksacks = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]
    for i, j, k in rucksacks:
        common = findcommon(i, j, k)
        score = wordscore(common)
        sum += score
    
    print(sum)