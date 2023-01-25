def mix(nums):
    original_pos = 0
    while original_pos < length:
        # get element that was originally at index i
        current_element = [x for x in nums if x[0] == original_pos][0]
        current_pos = nums.index(current_element)
        current_num = current_element[1]

        nums.remove(current_element)
        new_pos = (current_pos + current_num) % (length - 1)
        nums.insert(new_pos, current_element)

        original_pos += 1

    return nums


if __name__ == "__main__":

    with open("data/day20.txt") as f:
        original_nums = [int(x) for x in f.readlines()]

    length = len(original_nums)
    nums = [(i, num) for i, num in enumerate(original_nums)]

    nums = mix(nums)

    zero_element = [n for n in nums if n[1] == 0][0]
    zero_index = nums.index(zero_element)
    print(
        "Part 1:",
        sum([nums[(zero_index + k) % (length)][1] for k in [1000, 2000, 3000]]),
    )

    nums = [(i, num * 811589153) for i, num in enumerate(original_nums)]
    for _ in range(10):
        nums = mix(nums)

    zero_element = [n for n in nums if n[1] == 0][0]
    zero_index = nums.index(zero_element)
    print(
        "Part 2:",
        sum([nums[(zero_index + k) % (length)][1] for k in [1000, 2000, 3000]]),
    )
