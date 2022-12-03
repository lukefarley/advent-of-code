import random

# 7, x can't equal w since x >= 13
# 8, x == 0, so x = 1
# 9, y = 0
# 10, y = 25
# 11, y = 25
# 12, y = 26
# 13, z == 0, so z = 0
# 14, y = 0
# 15, y = w
# 16, y = w + 3
# 17, x == 1, so y = w + 3
# 18, z = w + 3

# after first block, x = 1, y = w1 + 3, z = w1 + 3

# if (w1 + 3) % 26 + 11 == w1, then

# 19,
# 20, x = 0
# 21, x = w1 + 3
# 22, x = (w1 + 3) % 26
# 23, z = w1 + 3
# 24, x = ((w1 + 3) % 26) + 11
# 25, if w2 = ((w1 + 3) % 26) + 11, then x = 1, else 0, -- here, it has to be 0, w2 < 11
# 26, x = 1 since x == 0
# 27, y = 0
# 28, y = 25
# 29, y = 25
# 30, y = 26
# 31, z = (w1 + 3) * 26
# 32, y = 0
# 33, y = w2
# 34, y = w2 + 12
# 35, y = w2 + 12
# 36, z = (w1 + 3) * 26 + (w2 + 12)

# after second block, x = 1, y = w2 + 12, z = (w1 + 3) * 26 + (w2 + 12)

# 37,
# 38, x = 0
# 39, x = (w1 + 3) * 26 + (w2 + 12)
# 40, x = ((w1 + 3) * 26 + (w2 + 12)) % 26
# 41, z = (w1 + 3) * 26 + (w2 + 12)
# 42, x = (((w1 + 3) * 26 + (w2 + 12)) % 26) + 15
# 43, x = 0
# 44, x = 1
# 45, y = 0
# 46, y = 25
# 47, y = 25
# 48, y = 26
# 49, z = ((w1 + 3) * 26 + (w2 + 12)) * 26
# 50, y = 0
# 51, y = w3
# 52, y = w3 + 9
# 53, y = w3 + 9
# 54, z = ((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9

# after third block, x = 1, y = w3 + 9, z = ((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9

# 55,
# 56, x = 0
# 57, x = ((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9
# 58, x = (((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9) % 26
# 59, z = (((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9) // 26
# 60, x = (((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9) % 26 - 6
# 61, x = 1 if (w3 + 3 = w4) else 0
# 62, x = 0 if (w3 + 3 = w4) else 1
# 63, y = 0
# 64, y = 25
# 65, y = 0 (assuming w3 + 3 = w4)
# 66, y = 1
# 67, z = (((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9) // 26
# 68, y = 0
# 69, y = w4
# 70, y = w4 + 12
# 71, y = 0
# 72, z = (((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9) // 26

# after fourth block,
#   if w3 + 3 = w4,
#        x = 0, y = 0, z = (((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9) // 26
#   else


# 73
# 74, x = 0
# 75, x = (((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9) // 26
# 76, x = ((((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9) // 26) % 26
# 77, z = (((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9) // 26
# 78, x = ((((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9) // 26) % 26 + 15
# 79, x = 0
# 80, x = 1
# 81, y = 0
# 82, y = 25
# 83, y = 25
# 84, y = 26
# 85, z = (((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9) // 26 * 26
# 86, y = 0
# 87, y = w5
# 88, y = w5 + 2,
# 89, y = w5 + 2
# 90, z = (((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9) // 26 * 26 + w5 + 2

# after 5th block, x = 1, y = w5 + 2, z = (((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9) // 26 * 26 + w5 + 2

# 91,
# 92, x = 0
# 93, x = (((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9) // 26 * 26 + w5 + 2
# 94, x = ((((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9) // 26 * 26 + w5 + 2) % 26
# 95, z = (((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9) // 26 * 26 + w5 + 2 // 26
# 96, x = ((((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9) // 26 * 26 + w5 + 2) % 26 - 8
# 97, if w5 - 6 = w6, then x = 1 else x = 0
# 98, x = 0
# 99, y = 0
# 100, y = 25
# 101, y = 0
# 102, y = 1
# 103, z = (((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9) // 26 * 26 + w5 + 2 // 26
# 104, y = 0
# 105, y = w6
# 106, y = w6 + 1
# 107, y = 0
# 108, z = (((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9) // 26 * 26 + w5 + 2 // 26

# **  w5 - 6 = w6

# 109, w7
# 110, x = 0
# 111, x = (((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9) // 26 * 26 + w5 + 2 // 26
# 112, x = (((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9) // 26 * 26 + w5 + 2 // 26 % 26
# 113, z = (((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9) // 26 * 26 + w5 + 2 // 26 // 26
# 114, x = x = ((((w1 + 3) * 26 + (w2 + 12)) * 26 + w3 + 9) // 26 * 26 + w5 + 2 // 26) % 26 - 4
# 115,
# 116,
# 117,
# 118,
# 119,
# 120,
# 121,
# 122,
# 123,

# ** w6 + 4 = w7

# inp w
# mul x 0
# add x z
# mod x 26
# div z 1
# add x 13
# eql x w
# eql x 0
# mul y 0
# add y 25
# mul y x
# add y 1
# mul z y
# mul y 0
# add y w
# add y 3
# mul y x
# add z y


def evaluate(commands, input_vals, variables={}):
    if not variables:
        variables = {"w": 0, "x": 0, "y": 0, "z": 0}

    iter_input_vals = iter(input_vals)

    for command in commands:
        if command[0] == "inp":
            variables[command[1]] = next(iter_input_vals)
        if command[0] == "add":
            # print("add")
            first = command[1]
            second = command[2]
            if second in list(variables.keys()):
                variables[first] = variables[first] + variables[second]
            else:
                variables[first] = variables[first] + int(second)
        elif command[0] == "mod":
            # print("mod")
            first = command[1]
            if variables[first] < 0:
                raise ValueError("if command is mod, a must be >= 0")
            second = command[2]
            if second in list(variables.keys()):
                variables[first] = variables[first] % variables[second]
            else:
                variables[first] = variables[first] % int(second)
        elif command[0] == "mul":
            # print("mul")
            first = command[1]
            second = command[2]
            if second in list(variables.keys()):
                variables[first] = variables[first] * variables[second]
            else:
                variables[first] = variables[first] * int(second)
        elif command[0] == "div":
            # print("div")
            first = command[1]
            second = command[2]
            if second in list(variables.keys()):
                variables[first] = variables[first] // variables[second]
            else:
                variables[first] = variables[first] // int(second)
            if variables[first] < 0:
                variables[first] += 1
        elif command[0] == "eql":
            # print("eql")
            first = command[1]
            second = command[2]
            if second in list(variables.keys()):
                variables[first] = int(variables[first] == variables[second])
            else:
                variables[first] = int(variables[first] == int(second))

    return variables


if __name__ == "__main__":
    with open("data/day24.txt") as f:
        input_ = [x.strip().split(" ") for x in f.read().strip().split("\n")]

    inputs_ = [random.randint(1, 9) for _ in range(14)]
    print(inputs_)
    evaluate(input_, inputs_)

    evaluate(input_, [int(x) for x in list(str(1958223344556677))])

    subroutines = []
    for i in range(0, 252, 18):
        subroutines.append(input_[i : i + 18])

    s = (
        subroutines[0]
        + subroutines[1]
        + subroutines[2]
        + subroutines[3]
        + subroutines[4]
        + subroutines[5]
        + subroutines[6]
        + subroutines[7]
    )

    #  + subroutines[7] +
    # subroutines[8] + subroutines[9] + subroutines[10] + subroutines[11])
    #  + subroutines[8] + subroutines[9] +
    # subroutines[10] + subroutines[11] + subroutines[12])

    # w3 + 3 = w4
    # w5 - 6 = w6

    evaluate(s, [int(x) for x in list("9969939194999")])

    # results = []
    # for i in range(1, 10):
    #     inputs_ = [i]
    #     results.append(evaluate(subroutines[0], inputs_))

    # results = []
    # for i in range(1, 10):
    #     inputs_ = [i]
    #     results.append(evaluate(subroutines[1], inputs_, variables={'w': 9, 'x': 1, 'y': 12, 'z': 12}))

    # results = []
    # for i in range(1, 10):
    #     inputs_ = [i]
    #     results.append(evaluate(subroutines[2], inputs_, variables={'w': 9, 'x': 1, 'y': 21, 'z': 333}))

    # results = []
    # for i in range(1, 10):
    #     inputs_ = [i]
    #     results.append(evaluate(subroutines[3], inputs_, variables={'w': 9, 'x': 1, 'y': 18, 'z': 8676}))

    # results = []
    # for i in range(1, 10):
    #     inputs = [i]
    #     results.append(evaluate(subroutines[4], inputs_, variables={'w': 9, 'x': 1, 'y': 21, 'z': 8679}))

    # results = []
    # for i in range(1, 10):
    #     inputs = [i]
    #     results.append(evaluate(subroutines[5], inputs_, variables={'w': 9, 'x': 1, 'y': 21, 'z': 225665}))
