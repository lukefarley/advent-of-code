def make_options(adapters):
    options = {}
    for i in range(len(adapters) - 1):
        cur = adapters[i]
        cur_options = []
        for possible_next in adapters[i + 1 : min(len(adapters), i + 4)]:
            if possible_next <= cur + 3:
                cur_options.append(possible_next)
        options[cur] = cur_options
    return options


def get_num_paths(options):
    num_paths = 0
    for n in options:
        # print(options)
        # print('-'*50)
        if n == max(options):
            return 1
        for o in options[n]:
            rest_of_options = {k: v for k, v in options.items() if k >= o}
            num_paths += get_num_paths(rest_of_options)
        return num_paths


if __name__ == "__main__":
    with open("data/day10.txt") as f:
        adapters = [int(x.strip("\n")) for x in f.readlines()]

    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters.sort()

    diffs = []
    for i in range(len(adapters) - 1):
        diffs.append(adapters[i + 1] - adapters[i])
    print(diffs)
    print(
        "Part 1:", len([d for d in diffs if d == 1]) * len([d for d in diffs if d == 3])
    )

    options = make_options(adapters)

    t1 = get_num_paths({k: v for k, v in options.items() if k < 33})
    t2 = get_num_paths({k: v for k, v in options.items() if k >= 33 and k < 51})
    t3 = get_num_paths({k: v for k, v in options.items() if k >= 51 and k < 75})
    t4 = get_num_paths({k: v for k, v in options.items() if k >= 75 and k < 99})
    t5 = get_num_paths({k: v for k, v in options.items() if k >= 99 and k < 122})
    t6 = get_num_paths({k: v for k, v in options.items() if k >= 122})

    print("Part 2:", t1 * t2 * t3 * t4 * t5 * t6)
