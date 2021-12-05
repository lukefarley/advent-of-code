def parse_rule(rule):
    rule = rule.replace("bags", "bag")
    rule = rule.replace(".", "")
    z = rule.find("contain")
    color = rule[: z - 5]
    contains = rule[z + 8 :]
    if contains == "no other bag":
        return {color: {}}
    else:
        contains = [x.replace("bag", "").strip() for x in contains.split(", ")]

    contains = dict(zip([x[2:] for x in contains], [x[0] for x in contains]))
    return {color: contains}


def check_bag_for_sub_bag(bag, bags_dict, sub_bag="shiny gold"):
    sub_bags = list(bags_dict[bag].keys())

    if len(sub_bags) == 0:
        return 0
    elif sub_bag in sub_bags:
        return 1
    else:
        found = 0
        for sb in sub_bags:
            found += check_bag_for_sub_bag(sb, bags_dict)
        return found > 0


def count_bags(bag, bags_dict):
    sub_bags = list(bags_dict[bag].keys())
    if len(sub_bags) == 0:
        return 0
    else:
        total = 0
        for sb in sub_bags:
            num_sb = int(bags_dict[bag][sb])
            total += num_sb * (1 + count_bags(sb, bags_dict))
        return total


if __name__ == "__main__":
    with open("data/day_7_input.txt") as f:
        rules = [x.strip() for x in f.read().strip("\n").split("\n")]

    bags_dict = {k: v for d in [parse_rule(r) for r in rules] for k, v in d.items()}

    print(sum([check_bag_for_sub_bag(c, bags_dict) for c in list(bags_dict.keys())]))
    print(count_bags("shiny gold", bags_dict))
