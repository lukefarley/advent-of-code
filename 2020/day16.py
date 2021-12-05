import functools
import operator


def get_criteria(notes):
    categories = [crit.split(": ")[0] for crit in notes[0]]
    criteria = [crit.split(": ")[1].split(" or ") for crit in notes[0]]
    all_vals = []
    for c in criteria:
        vals = []
        for n in c:
            z = n.split("-")
            vals.append(list(range(int(z[0]), int(z[1]) + 1)))
        vals = functools.reduce(operator.add, vals)
        all_vals.append(vals)
    return dict(zip(categories, all_vals))


with open("data/day_16_input.txt") as f:
    notes = f.read().strip().split("\n\n")

notes = [section.split("\n") for section in notes]

nearby_tix = [[int(x) for x in t.split(",")] for t in notes[2][1:]]

criteria = get_criteria(notes)

invalid_nums = []
vals = functools.reduce(operator.add, list(criteria.values()))
invalid_tix = set()
for i, t in enumerate(nearby_tix):
    for num in t:
        if num not in vals:
            invalid_tix.add(i)
            invalid_nums.append(num)

valid_tix = [tik for i, tik in enumerate(nearby_tix) if i not in invalid_tix]
cant = {c: set() for c in list(criteria.keys())}
for t1 in valid_tix:
    for c in criteria:
        for i, num in enumerate(t1):
            if num not in criteria[c]:
                cant[c].add(i)

num_available = len(valid_tix[0])
available = set(range(num_available))
taken = {}
while num_available > 0:
    d = {k: v for k, v in cant.items() if len(v) == num_available - 1}
    name = list(d.keys())[0]
    val = list(available - list(d.values())[0])[0]
    taken[name] = val
    available = available - (available - list(d.values())[0])
    num_available -= 1


my_ticket = notes[1][1].split(",")
departure_idx = list({k: v for k, v in taken.items() if "departure" in k}.values())
functools.reduce(
    operator.mul, [int(num) for i, num in enumerate(my_ticket) if i in departure_idx]
)
