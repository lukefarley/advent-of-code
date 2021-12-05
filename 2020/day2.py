def check_password(password: str, part: int = 1):
    colon_pos = password.find(":")
    letter = password[colon_pos - 1]

    dash_pos = password.find("-")

    nmin = int(password[:dash_pos])
    nmax = int(password[dash_pos + 1 : colon_pos - 2])

    pword_str = password[colon_pos + 2 :]

    if part == 1:
        num_letter = pword_str.count(letter)
        return num_letter >= nmin and num_letter <= nmax
    if part == 2:
        return (pword_str[nmin - 1] == letter) ^ (pword_str[nmax - 1] == letter)


if __name__ == "__main__":
    f = open("data/day_2_input.txt")
    passwords = f.read().splitlines()
    f.close()

    print("Part 1:", sum([check_password(p, 1) for p in passwords]))
    print("Part 2:", sum([check_password(p, 2) for p in passwords]))
