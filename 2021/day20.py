# tst = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
# #..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
# .######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
# .#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
# .#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
# ...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
# ..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#
# \n
# #..#.
# #....
# ##..#
# ..#..
# ..###""".split("\n\n")


# pad
def pad_img(img, n=1, char="."):
    img = [
        [char for _ in range(n)] + img[i] + [char for _ in range(n)]
        for i in range(len(img))
    ]
    for _ in range(n):
        img.append([char for _ in range(len(img[0]))])
        img.append([char for _ in range(len(img[0]))])

    img = img[-n:] + img[:-n]
    return img


def get_algo_pos(img, i, j):
    inputs_ = []
    points = [
        (i - 1, j - 1),
        (i, j - 1),
        (i + 1, j - 1),
        (i - 1, j),
        (i, j),
        (i + 1, j),
        (i - 1, j + 1),
        (i, j + 1),
        (i + 1, j + 1),
    ]
    # print(points)
    for p in points:
        inputs_.append(img[p[1]][p[0]])
    inputs_ = ["1" if x == "#" else "0" for x in inputs_]
    return int("".join(inputs_), 2)


def get_new_pixel_val(img, i, j, algo):
    return algo[get_algo_pos(img, i, j)]


def apply_enhancement(img, algo):
    new_img = [i.copy() for i in img]
    for i in range(1, len(img) - 1):
        for j in range(1, len(img) - 1):
            new_img[j][i] = get_new_pixel_val(img, i, j, algo)

    new_img = new_img[2 : len(new_img) - 2]
    new_img = [r[2 : len(r) - 2] for r in new_img]
    border_char = new_img[0][0]
    print(border_char)
    new_img = pad_img(new_img, n=5, char=border_char)
    return new_img


with open("data/day20.txt") as f:
    input_ = f.read().split("\n\n")

algo = input_[0]
img = [list(x) for x in input_[1].split("\n")]
img = pad_img(img, 10)
# img = apply_enhancement(img, algo)


# for i in range(len(img)):
#     for j in range(len(img)-2, len(img)):
#         img[i][j] = "#"
#         img[j][i] = "#"

# for i in range(len(img)):
#     for j in range(2):
#         img[i][j] = "#"
#         img[j][i] = "#"

# for i in range(len(img)):
#     for j in range(1, 2):
#         img[i][j] = "."
#         img[j][i] = "."

# for i in range(len(img)):
#     for j in range(len(img)-2, len(img)-1):
#         img[i][j] = "."
#         img[j][i] = "."


# for _ in range(2):
#     img = apply_enhancement(img, algo)

for _ in range(50):
    img = apply_enhancement(img, algo)

print(sum([sum([1 if ij == "#" else 0 for ij in i]) for i in img]))
