import string


def get_common_answers(group):
    result = dict(zip(list(string.ascii_letters[:26]), [0] * 26))
    for letter in list(result.keys()):
        for person in group:
            if letter in person:
                result[letter] += 1

    return [r for r in result if result[r] == len(group)]


if __name__ == "__main__":
    with open("data/day_6_input.txt", "r") as f:
        print(
            sum([len(set(x.replace("\n", "").strip())) for x in f.read().split("\n\n")])
        )
    with open("data/day_6_input.txt", "r") as f:
        print(
            sum(
                [
                    len(get_common_answers(x.strip().split("\n")))
                    for x in f.read().split("\n\n")
                ]
            )
        )
