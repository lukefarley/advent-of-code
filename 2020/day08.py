def get_next_instruction(code, i):
    val = int(code[i][4:])

    if code[i][:3] == "acc":
        acc = val
        next_instruction = i + 1
    elif code[i][:3] == "jmp":
        acc = 0
        next_instruction = i + val
    else:
        acc = 0
        next_instruction = i + 1

    return next_instruction, acc


if __name__ == "__main__":
    with open("data/day_8_input.txt") as f:
        code = [x for x in f.read().strip().split("\n")]

    instructions = [0]
    accumulator = 0
    nxt = 0

    last = len(code)

    # # part 1
    # while True:
    #     print(instructions)
    #     nxt, acc = get_next_instruction(code, nxt)
    #     # print(acc, nxt)
    #     accumulator += acc
    #     if nxt in instructions:
    #         break
    #     instructions.append(nxt)

    # print(accumulator)

    # part 2
    for i in range(300):
        print(i)
        instructions = []
        accumulator = 0
        nxt = 0
        last = len(code)
        jumps_seen = 0
        # nops_seen = 0
        cur = 0
        while cur not in instructions:
            # print(instructions)

            val = int(code[cur][4:])

            if code[cur][:3] == "acc":
                accumulator += val
                next_instruction = cur + 1
            elif code[cur][:3] == "jmp":
                # next_instruction = cur + val
                if jumps_seen == i:
                    # treat as nop
                    next_instruction = cur + 1
                else:
                    next_instruction = cur + val
                jumps_seen += 1
            else:
                next_instruction = cur + 1
                # if nops_seen == i:
                #     #treat as jmp
                #     next_instruction = cur + val
                # else:
                #     next_instruction = cur + 1
                # nops_seen += 1

            instructions.append(cur)

            # if next_instruction in instructions:
            #     break
            if next_instruction == len(code):
                print("end reached! accumulator:", accumulator)
                break

            cur = next_instruction
