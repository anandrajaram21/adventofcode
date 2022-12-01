with open("input.txt") as f:
    calories = []
    temp = []
    for i in f.readlines():
        if i == "\n":
            calories.append(temp)
            temp = []
        else:
            temp.append(i)
    
    calories.append(temp)

    for i in range(len(calories)):
        calories[i] = [int(j) for j in calories[i]]
        calories[i] = sum(calories[i])

    # Print sum of 3 maximum values
    print(sum(sorted(calories)[-3:]))