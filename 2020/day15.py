TEST = """0,3,6"""
start = [int(x) for x in TEST.split(",")]


def get_nth_num(start, n):
    nums = start.copy()
    i = len(nums)
    while True:
        if nums[-1] not in nums[:-1]:
            nums.append(0)
            i += 1
        else:
            # nums[-1] in nums[:-1]
            nums.append(list(reversed(nums[:-1])).index(nums[-1]) + 1)
            i += 1
        if i == n:
            return nums


def get_nth_num2(start, n):
    i = len(start)
    last_seen_at = dict(zip(start, list(range(i))))
    seen = set(last_seen_at.keys())
    next_num = 0
    while True:
        # print(i, last_seen_at, next_num)
        if next_num in seen:
            prev_num = next_num
            next_num = i - last_seen_at[prev_num]
            last_seen_at[prev_num] = i
        else:
            prev_num = next_num
            next_num = 0
            last_seen_at[prev_num] = i
            seen.add(prev_num)

        if i == n - 1:
            return prev_num
        i += 1


# with open("data/day_15_input.txt") as f:
#     start = [int(x) for x in f.read().strip().split(",")]

start = [2, 0, 1, 7, 4, 14, 18]

# answer = get_nth_num(start, 2020)
answer = get_nth_num2(start, 30000000)
print(answer)

# n = 30000000
# nums = start.copy()
# i = len(nums)

# while True:
#     if nums[-1] not in nums[:-1]:
#         nums.append(0)
#         i += 1

#     else:
#         # nums[-1] in nums[:-1]
#         nums.append(list(reversed(nums[:-1])).index(nums[-1]) + 1)
#         i += 1
#     if i == n:
#         print(i, nums[-1])
#         break
#     if len(nums) % 1000 == 0:
#         nums = nums[-500:]
#     if i % 100000 == 0:
#         print(i)
