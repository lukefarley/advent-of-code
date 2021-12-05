import re

TEST = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""

with open("data/day_19_input.txt") as f:
    rules, messages = f.read().strip().split("\n\n")
    rules = rules.split("\n")
    rules = dict(
        zip(
            [int(rule[: rule.find(":")]) for rule in rules],
            [rule[rule.find(":") + 2 :] for rule in rules],
        )
    )
    messages = messages.split("\n")


# rules, messages = TEST.split("\n\n")
# rules = rules.split("\n")
# rules = dict(zip([int(rule[:rule.find(":")]) for rule in rules],
#                  [rule[rule.find(":")+2:] for rule in rules]))

# messages = messages.split("\n")


def parse_rule(rules, num):
    z = rules[num].split(" ")
    message = ""

    if "|" in z:
        message = "("

    for zi in z:
        if zi == "|":
            message += "|"
        elif zi == '"a"':
            message += "a"
        elif zi == '"b"':
            message += "b"
        else:
            message += parse_rule(rules, int(zi))

    if "|" in z:
        message += ")"

    return message


# messages = []
def get_valid_messages(legend):
    parens = re.compile("\([^\(\)]+\)")
    if parens.search(legend):
        span = parens.search(legend).span()
        options = parens.search(legend)[0][1:-1].split("|")

        for o in options:
            message = legend[: span[0]] + o + legend[span[1] :]
            get_valid_messages(message)
    else:
        print(legend)
        messages.append(legend)


idx = set(list(range(len(x))))
while parens.search(x):
    span = parens.search(x).span()
    idx = idx - set(span)
    x = x[: span[0]] + x[span[1] :]
