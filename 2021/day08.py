import functools
import operator


def map_to_numbers(input):
    lookup = {}

    lookup[1] = [set(x) for x in input if len(x) == 2][0]
    lookup[4] = [set(x) for x in input if len(x) == 4][0]
    lookup[7] = [set(x) for x in input if len(x) == 3][0]
    lookup[8] = [set(x) for x in input if len(x) == 7][0]

    possible_6s = [set(x) for x in input if len(x) == 6]
    possible_5s = [set(x) for x in input if len(x) == 5]

    # we can get 9 by figuring out which one of length 6 has all the elements of 4
    lookup[9] = [x for x in possible_6s if x.issuperset(lookup[4])][0]
    possible_6s.remove(lookup[9])

    # we can get 0 by figuring out which remaining ones of length 6 have all elements of 1
    lookup[0] = [x for x in possible_6s if x.issuperset(lookup[1])][0]
    possible_6s.remove(lookup[0])

    # 6 is the only one of length 6 remaining
    lookup[6] = possible_6s[0]

    # we can get 3 by figuring out which one of length 5 has all elements of 7
    lookup[3] = [x for x in possible_5s if x.issuperset(lookup[7])][0]
    possible_5s.remove(lookup[3])

    # we can get 5 by figuring out which remaining ones of length 5 are contained within 9
    lookup[5] = [x for x in possible_5s if x.issubset(lookup[9])][0]
    possible_5s.remove(lookup[5])

    # 2 is the only one of length 5 remaining
    lookup[2] = possible_5s[0]

    return {"".join(sorted(v)): k for k, v in lookup.items()}


if __name__ == "__main__":

    with open("data/day08.txt") as f:
        raw = [line.strip().split(" | ") for line in f.readlines()]

    inputs = [x[0].split(" ") for x in raw]
    outputs = [x[1].split(" ") for x in raw]

    output_lengths = [len(output) for output in functools.reduce(operator.add, outputs)]
    print("Part 1:", len([x for x in output_lengths if x in [2, 4, 3, 7]]))

    total = 0
    for i in range(len(inputs)):
        lookup = map_to_numbers(inputs[i])
        total += int("".join([str(lookup["".join(sorted(k))]) for k in outputs[i]]))

    print("Part 2:", total)
