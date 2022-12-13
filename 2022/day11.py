import re


def get_remainders(item):
    return {
        2: item % 2,
        3: item % 3,
        5: item % 5,
        7: item % 7,
        11: item % 11,
        13: item % 13,
        17: item % 17,
        19: item % 19,
        23: item % 23,
    }

    
def make_function(string_operation):
    return eval("lambda old:" + string_operation)


def make_remainder_function(string_operation, N):
    return eval("lambda old: (" + string_operation + f") % {N}")


class Monkey:
    def __init__(
        self,
        monkey_id,
        items,
        item_remainders,
        operation_str,
        operation,
        test_div,
        monkey_if_true,
        monkey_if_false
    ):
        self.id = monkey_id
        self.items = items
        self.item_remainders = item_remainders
        self.operation_str = operation_str
        self.operation = operation
        self.test_div = test_div
        self.monkey_if_true = monkey_if_true
        self.monkey_if_false = monkey_if_false
        self.remainder_operations = {
            k: make_remainder_function(self.operation_str, k)
            for k in get_remainders(1).keys()
        }
        self.num_inspections = 0


    def __iter__(self):
        return iter(self)

def parse_monkey_desc(monkey_desc):
    monkey_desc = monkey_desc.split("\n")

    monkey_id = int(re.findall("[0-9]+", monkey_desc[0])[0])

    items = [int(x) for x in re.findall("[0-9]+", monkey_desc[1])]
    remainders = [get_remainders(item) for item in items]

    operation_str = monkey_desc[2].split("= ")[1]
    operation = make_function(monkey_desc[2].split("= ")[1])

    test_div = int(re.findall("[0-9]+", monkey_desc[3])[0])
    monkey_if_true = int(re.findall("[0-9]+", monkey_desc[4])[0])
    monkey_if_false = int(re.findall("[0-9]+", monkey_desc[5])[0])

    return Monkey(
        monkey_id=monkey_id,
        items=items,
        item_remainders=remainders,
        operation_str=operation_str,
        operation=operation,
        test_div=test_div,
        monkey_if_true=monkey_if_true,
        monkey_if_false=monkey_if_false
    )


def do_round1(monkeys):

    for monkey in monkeys:
        for item in monkey.items:
            item = monkey.operation(item) // 3
            if item % monkey.test_div == 0:
                monkeys[monkey.monkey_if_true].items.append(item)
            else:
                monkeys[monkey.monkey_if_false].items.append(item)
            monkey.items = monkey.items[1:]
            monkey.num_inspections += 1

    return monkeys


def do_round2(monkeys):

    for monkey in monkeys:
        for item in monkey.item_remainders:
            for ir in item:
                item[ir] = monkey.remainder_operations[ir](item[ir])

            if item[monkey.test_div] == 0:
                monkeys[monkey.monkey_if_true].item_remainders.append(item)
            else:
                monkeys[monkey.monkey_if_false].item_remainders.append(item)

            monkey.item_remainders = monkey.item_remainders[1:]
            monkey.num_inspections += 1

    return monkeys


if __name__ == "__main__":
    with open("data/day11.txt") as f:
        raw = [x.strip() for x in f.read().split("\n\n")]

    monkeys = []
    for i in range(len(raw)):
        monkeys.append(parse_monkey_desc(raw[i]))

    for _ in range(20):
        monkeys = do_round1(monkeys)

    num_inspections = sorted([m.num_inspections for m in monkeys])
    print("Part 1:", num_inspections[-1] * num_inspections[-2])

    monkeys = []
    for i in range(len(raw)):
        monkeys.append(parse_monkey_desc(raw[i]))

    for _ in range(10000):
        monkeys = do_round2(monkeys)

    num_inspections = sorted([m.num_inspections for m in monkeys])
    print("Part 2:", num_inspections[-1] * num_inspections[-2])
