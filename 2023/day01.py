import re


NUM_WORDS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

NUM_LOOKUP = dict(zip(NUM_WORDS, list(range(1, 10))))


def process_line(line):
    nums = re.findall("\d", line)
    first_number = nums[0]
    last_number = nums[-1]

    return int(first_number + last_number)


def format_num(num):
    if len(num) == 1:
        return str(num)
    else:
        return str(NUM_LOOKUP[num])


def process_line2(line):
    nums = re.findall("\d|" + "|".join(NUM_WORDS), line)
    first_number = format_num(nums[0])
    last_number = format_num(nums[-1])

    return int(first_number + last_number)


if __name__ == "__main__":

    with open("data/day01.txt") as f:
        doc = [x.strip() for x in f.readlines()]

    vals = [process_line(line) for line in doc]
    print("Part 1:", sum(vals))

    vals2 = [process_line2(line) for line in doc]
    print("Part 2:", sum(vals2))
