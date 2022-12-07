import re


def read_stacks(raw_stacks):
    string_stacks = raw_stacks.split("\n")

    stacks = [[] for i in range(len(string_stacks))]

    for j in range(9):
        for i in range(len(string_stacks) - 2, -1, -1):
            next_crate = string_stacks[i][j * 4 : j * 4 + 3]
            if "[" in next_crate:
                stacks[j].append(next_crate.replace("[", "").replace("]", ""))

    return stacks


def read_instructions(raw_instructions):
    instructions = raw_instructions.split("\n")

    return [
        [int(x) for x in re.findall("[0-9]+", instruction)]
        for instruction in instructions
    ]


def move9000(stacks, instruction):
    num_to_move, starting_stack, ending_stack = instruction
    for _ in range(num_to_move):
        stacks[ending_stack - 1].append(stacks[starting_stack - 1].pop())

    return stacks


def move9001(stacks, instruction):
    num_to_move, starting_stack, ending_stack = instruction
    if num_to_move == 1:
        return move9000(stacks, instruction)
    else:
        for crate in stacks[starting_stack - 1][-num_to_move:]:
            stacks[ending_stack - 1].append(crate)
        stacks[starting_stack - 1] = stacks[starting_stack - 1][:-num_to_move]

    return stacks


if __name__ == "__main__":
    with open("data/day05.txt") as f:
        raw_stacks, raw_instructions = f.read().split("\n\n")

    stacks = read_stacks(raw_stacks)
    instructions = read_instructions(raw_instructions)  

    for instruction in instructions:
        stacks = move9000(stacks, instruction)

    print("Part 1:", "".join([s[-1] for s in stacks]))

    stacks = read_stacks(raw_stacks)

    for instruction in instructions:
        stacks = move9001(stacks, instruction)

    print("Part 2:", "".join([s[-1] for s in stacks]))
