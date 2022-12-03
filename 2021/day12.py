import functools
import operator

# start: [HN, dc, kj]
# end: [HN]
# HN: [dc, start, end]
# dc: [end, HN, LN, kj]
# jk: [sa, HN, dc]

tst = """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".split(
    "\n"
)

# tst = """dc-end
# HN-start
# start-kj
# dc-start
# dc-HN
# LN-dc
# HN-end
# kj-sa
# kj-HN
# kj-dc""".split("\n")


def parse(raw):
    caves = [x.split("-") for x in raw]
    unique_caves = list(set(functools.reduce(operator.add, caves)))

    cave_map = dict(zip(unique_caves, [[] for _ in range(len(unique_caves))]))

    for key_val in caves:
        cave_map[key_val[0]].append(key_val[1])
        cave_map[key_val[1]].append(key_val[0])

    return cave_map


def get_paths(cave_map, cave="start", current_path=[], all_paths=[]):

    current_path.append(cave)

    if cave == "end":
        # return current_path
        if current_path[0] == "start":
            return current_path
    else:
        next_caves = cave_map[cave]
        if "start" in next_caves:
            next_caves.remove("start")

        small_next_caves = [nc for nc in next_caves if nc.lower() == nc]

        small_caves_lookup = {}
        for sc in list(set([x for x in next_caves + current_path if x.lower() == x])):
            small_caves_lookup[sc] = current_path.count(sc)

        if "end" in small_next_caves:
            small_next_caves.remove("end")

        for nc in next_caves:
            # if small_caves_rule == 1:
            #     small_caves_check =
            # else:
            #     small_caves_check = nc in small_next_caves and nc in current_path and any([x > 1 for x in list(small_caves_lookup.values())])

            if (
                nc in small_next_caves
                and nc in current_path
                and any([x > 1 for x in list(small_caves_lookup.values())])
            ):
                continue
            cp = current_path.copy()
            all_paths.append(get_paths(cave_map, nc, cp, all_paths))

    # return [p for p in all_paths if isinstance(p[0], str)]
    return all_paths


if __name__ == "__main__":
    with open("data/day12.txt") as f:
        raw = [x.strip() for x in f.readlines()]

    cave_map = parse(raw)
    paths = get_paths(cave_map, "start")

    print("Part 1:", len([p for p in paths if isinstance(p[0], str)]))

    paths = get_paths(cave_map, "start")
    print("Part 2:", len([p for p in paths if isinstance(p[0], str)]))
