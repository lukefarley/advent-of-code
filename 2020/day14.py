import itertools

TEST = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

mask = TEST[7:43]
inp = [x for x in TEST.split("\n")[1:]]
addresses = [int(x[x.index("[") + 1 : x.index("]")]) for x in inp]
values = [int(x[x.index("=") + 2 :]) for x in inp]

instructions = list(zip(addresses, values))


def make_binary(num):
    return "{0:b}".format(num).zfill(36)


def apply_string(current, val):
    new = current
    for i, c in enumerate(val):
        if c != "X":
            if i > 0 and i < len(val) - 1:
                new = new[:i] + c + new[i + 1 :]
            if i == len(val) - 1:
                new = new[:i] + c
            if i == 0:
                new = c + new[i + 1 :]
    return new


def apply_instructions(mem_dict, instructions):
    mask = instructions[0]
    addresses = [int(x[x.index("[") + 1 : x.index("]")]) for x in instructions[1:]]
    values = [int(x[x.index("=") + 2 :]) for x in instructions[1:]]

    for a, v in list(zip(addresses, values)):
        if a not in mem_dict:
            mem_dict[a] = make_binary(0)
        mem_dict[a] = apply_string(mem_dict[a], apply_string(make_binary(v), mask))

    return mem_dict


def apply_mask_v2(current, mask):
    new = current
    for i, c in enumerate(mask):
        if c == "0":
            continue
        else:
            if i > 0 and i < len(mask) - 1:
                new = new[:i] + c + new[i + 1 :]
            if i == len(mask) - 1:
                new = new[:i] + c
            if i == 0:
                new = c + new[i + 1 :]
    return new


def get_combinations(x):
    combinations = []

    loc_Xs = []
    for i, c in enumerate(x):
        if c == "X":
            loc_Xs.append(i)
    vals = list(itertools.product("01", repeat=len(loc_Xs)))
    for val in vals:
        new = x
        for i, c in enumerate(val):
            if loc_Xs[i] == 0:
                new = str(c) + new[loc_Xs[i] + 1 :]
            if loc_Xs[i] > 0 and loc_Xs[i] < len(x) - 1:
                new = new[: loc_Xs[i]] + str(c) + new[loc_Xs[i] + 1 :]
            if loc_Xs[i] == len(x) - 1:
                new = new[: loc_Xs[i]] + str(c)
        combinations.append(new)

    return combinations


def apply_instructions2(mem_dict, instructions):
    mask = instructions[0]
    addresses = [int(x[x.index("[") + 1 : x.index("]")]) for x in instructions[1:]]
    values = [int(x[x.index("=") + 2 :]) for x in instructions[1:]]

    for a, v in list(zip(addresses, values)):
        binary_address = make_binary(a)
        masked_address = apply_mask_v2(binary_address, mask)
        all_addresses = get_combinations(masked_address)
        for ad in [int(x, 2) for x in all_addresses]:
            if ad not in mem_dict:
                mem_dict[ad] = make_binary(0)
            mem_dict[ad] = apply_string(mem_dict[ad], make_binary(v))

    return mem_dict


with open("data/day14.txt") as f:
    instructions = [
        x.strip().split("\n") for x in f.read().strip().split("mask = ")[1:]
    ]

# test2 = """mask = 000000000000000000000000000000X1001X
# mem[42] = 100
# mask = 00000000000000000000000000000000X0XX
# mem[26] = 1"""

# instructions = [x.strip().split("\n") for x in test2.strip().split("mask = ")[1:]]
# mem_dict = {}
# for i in instructions:
#     mem_dict = apply_instructions2(mem_dict, i)


# mem_dict = {}
# for i in instructions:
#     mem_dict = apply_instructions(mem_dict, i)

mem_dict = {}
for i in instructions:
    mem_dict = apply_instructions2(mem_dict, i)

# print(mem_dict)

print(sum([int(x, 2) for x in list(mem_dict.values())]))
