import string

def push(stack, item):
    stack.append(item)

def pop(stack):
    return stack.pop()

def peek(stack):
    return stack[-1]

def move(stack1, stack2):
    push(stack2, pop(stack1))

def split_line(line):
    # Split the line at every 4 characters
    return [line[i] for i in range(1, len(line), 4)]

with open("input.txt") as f:
    contents = f.readlines()
    stackNum = 0
    stacks = []
    for i in range(len(contents)):
        if "1" in contents[i]:
            stacks = [[] for j in range(i+1)]
            stackNum = i
            break

    lines = [split_line(line) for line in contents[:stackNum]]
    lines = lines[::-1]

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == " ":
                continue
            push(stacks[j], lines[i][j])
    
    instruction_lines = contents[stackNum+2:]
    instruction_lines = [line.strip() for line in instruction_lines]

    for i in range(len(instruction_lines)):
        instruction = instruction_lines[i]
        instruction = instruction.replace("move ", "")
        f_in = instruction.find("from")
        num = int(instruction[:f_in])
        instruction = instruction[f_in:]
        instruction = instruction.replace("from ", "")
        f_to = instruction.find("to")
        from_stack = int(instruction[:f_to])
        to_stack = int(instruction[f_to+3:])

        instruction_lines[i] = (num, from_stack, to_stack)
    
    for num, from_stack, to_stack in instruction_lines:
        for i in range(num):
            move(stacks[from_stack-1], stacks[to_stack-1])

    final_string = ""
    for i in stacks:
        final_string += peek(i)

    print(final_string)
