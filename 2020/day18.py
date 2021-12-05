import re
import functools
import operator

TEST = """2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""

hw = TEST.strip().split("\n")


def evaluate(expr):
    s = expr.split(" ")
    answer = eval(s[0])
    ops = []
    for i in range(1, len(s), 2):
        ops.append(" ".join(s[i : i + 2]))
    for o in ops:
        print(str(answer) + o)
        answer = eval(str(answer) + o)
    return answer


def evaluate2(expr):
    s = expr.split("*")
    return functools.reduce(operator.mul, [eval(si) for si in s])


def evaluate_all(expr):
    parens = re.compile("\([^\(\)]+\)")
    z = 0
    if parens.search(expr):
        span = parens.search(expr).span()
        expr = (
            expr[: span[0]]
            + str(evaluate2(expr[span[0] + 1 : span[1] - 1]))
            + expr[span[1] :]
        )
        print("new expr:", expr)
        return evaluate_all(expr)
    return evaluate2(expr)


with open("data/day18.txt") as f:
    hw = f.read().strip().split("\n")
