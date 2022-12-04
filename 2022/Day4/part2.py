def overlaps(i1, i2, j1, j2):
    r1 = set(range(i1, i2+1))
    r2 = set(range(j1, j2+1))

    if r1.intersection(r2):
        return True
    return False

with open("input.txt") as f:
    contents = f.readlines()
    contents = [i.strip() for i in contents]
    ranges = [i.split(",") for i in contents]

    count = 0

    for i in ranges:
        for j in range(len(i)):
            i[j] = [int(k) for k in i[j].split("-")]

    for i in ranges:
        r1 = i[0]
        r2 = i[1]

        if overlaps(r1[0], r1[1], r2[0], r2[1]):
            count += 1

    print(count)