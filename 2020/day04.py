import re


def make_passport_dict(p):

    plist = p.split(" ")
    k = [plist[i] for i in range(0, len(plist), 2)]
    v = [plist[i] for i in range(1, len(plist), 2)]

    return dict(zip(k, v))


def check_passport_ids(p):
    ids = ["pid", "hcl", "eyr", "iyr", "hgt", "byr", "ecl"]
    return sum([i in p for i in ids]) == len(ids)


def check_passport_vals(p):
    if not check_passport_ids(p):
        return False

    p = make_passport_dict(p)
    if int(p["byr"]) < 1920 or int(p["byr"]) > 2002:
        return False
    if int(p["iyr"]) < 2010 or int(p["iyr"]) > 2020:
        return False
    if int(p["eyr"]) < 2020 or int(p["eyr"]) > 2030:
        return False

    # height
    if "cm" in p["hgt"]:
        z = int(p["hgt"].replace("cm", ""))
        if z < 150 or z > 193:
            return False
    elif "in" in p["hgt"]:
        z = int(p["hgt"].replace("in", ""))
        if z < 59 or z > 76:
            return False
    else:
        return False

    # hair color
    valid_chars = [str(z) for z in list(range(0, 10))] + ["a", "b", "c", "d", "e", "f"]
    if p["hcl"][0] != "#":
        return False
    if len(p["hcl"].replace("#", "")) != 6:
        return False
    if any([s not in valid_chars for s in p["hcl"].replace("#", "")]):
        return False

    # eye color
    valid = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if p["ecl"] not in valid:
        return False

    # pid
    if len(p["pid"]) != 9:
        return False
    if any([s not in [str(z) for z in list(range(0, 10))] for s in p["pid"]]):
        return False

    return True


if __name__ == "__main__":
    f = open("data/day04.txt")
    passports = [
        p.replace("\n", " ").strip().replace(":", " ") for p in f.read().split("\n\n")
    ]
    f.close()

    print(sum([check_passport_ids(p) for p in passports]))
    print(sum([check_passport_vals(p) for p in passports]))
