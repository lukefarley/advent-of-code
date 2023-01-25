def do_task(monkeys, monkey_name):
    val = 0

    if "+" in monkeys[monkey_name]:
        monkey1, monkey2 = monkeys[monkey_name].split(" + ")
        val += do_task(monkeys, monkey1) + do_task(monkeys, monkey2)
    elif "-" in monkeys[monkey_name]:
        monkey1, monkey2 = monkeys[monkey_name].split(" - ")
        val += do_task(monkeys, monkey1) - do_task(monkeys, monkey2)
    elif "*" in monkeys[monkey_name]:
        monkey1, monkey2 = monkeys[monkey_name].split(" * ")
        val += do_task(monkeys, monkey1) * do_task(monkeys, monkey2)
    elif "/" in monkeys[monkey_name]:
        monkey1, monkey2 = monkeys[monkey_name].split(" / ")
        val += do_task(monkeys, monkey1) / do_task(monkeys, monkey2)
    else:
        val = int(monkeys[monkey_name])

    return val


def print_task(monkeys, monkey_name):
    operation_str = ""

    if "+" in monkeys[monkey_name]:
        monkey1, monkey2 = monkeys[monkey_name].split(" + ")
        operation_str += (
            "("
            + print_task(monkeys, monkey1)
            + " + "
            + print_task(monkeys, monkey2)
            + ")"
        )
    elif "-" in monkeys[monkey_name]:
        monkey1, monkey2 = monkeys[monkey_name].split(" - ")
        operation_str += (
            "("
            + print_task(monkeys, monkey1)
            + " - "
            + print_task(monkeys, monkey2)
            + ")"
        )
    elif "*" in monkeys[monkey_name]:
        monkey1, monkey2 = monkeys[monkey_name].split(" * ")
        operation_str += (
            "("
            + print_task(monkeys, monkey1)
            + " * "
            + print_task(monkeys, monkey2)
            + ")"
        )
    elif "/" in monkeys[monkey_name]:
        monkey1, monkey2 = monkeys[monkey_name].split(" / ")
        operation_str += (
            "("
            + print_task(monkeys, monkey1)
            + " / "
            + print_task(monkeys, monkey2)
            + ")"
        )
    elif "=" in monkeys[monkey_name]:
        monkey1, monkey2 = monkeys[monkey_name].split(" = ")
        operation_str += (
            "("
            + print_task(monkeys, monkey1)
            + " = "
            + print_task(monkeys, monkey2)
            + ")"
        )

    else:
        operation_str = str(monkeys[monkey_name])

    return operation_str


def evaluate_expression(expression):
    for _ in range(2000):
        for i, char in enumerate(expression):
            if char == "(":
                last_left_paren = i
            elif char == ")":
                if "x" in expression[last_left_paren : i + 1]:
                    continue
                else:
                    expression = (
                        expression[:last_left_paren]
                        + str(eval(expression[last_left_paren : i + 1]))
                        + expression[i + 1 :]
                    )
                    break
    return expression


if __name__ == "__main__":

    with open("data/day21.txt") as f:
        raw = [x.strip() for x in f.readlines()]

    monkeys = {}
    for monkey in raw:
        name, task = monkey.split(": ")
        monkeys[name] = task

    do_task(monkeys, "root")

    monkeys["root"] = monkeys["root"].replace(" + ", " = ")
    monkeys["humn"] = "x"

    monkeys["humn"] = "55466149605646"

    expression = print_task(monkeys, "root")
    left, right = expression.split(" = ")

    left_reduced = int(evaluate_expression(left[1:]).replace(".0", ""))
    right_reduced = int(evaluate_expression(right[:-1]).replace(".0", ""))

    # left_reduced = evaluate_expression(left[1:])
    # right_reduced = evaluate_expression(right[:-1])
    off_by = right_reduced - left_reduced
