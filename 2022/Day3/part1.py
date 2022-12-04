def findcommon(a, b):
    for i in a:
        for j in b:
            if i == j:
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
    # Split each line into two halves
    rucksacks = [[i[:len(i)//2], i[len(i)//2:]] for i in rucksacks]
    for i, j in rucksacks:
        common = findcommon(i, j)
        score = wordscore(common)
        sum += score
    
    print(sum)