import functools

hex_lookup = """0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110
7 = 0111
8 = 1000
9 = 1001
A = 1010
B = 1011
C = 1100
D = 1101
E = 1110
F = 1111""".split(
    "\n"
)

hex_lookup = [x.split(" = ") for x in hex_lookup]
hex_lookup = dict(zip([x[0] for x in hex_lookup], [x[1] for x in hex_lookup]))


def parse_hex(hex_string, hex_lookup):
    result = ""
    for char in hex_string:
        result += hex_lookup[char]
    return result


def process_subpacket_vals(subpacket_vals, type_id):
    if type_id == 0:
        val = sum(subpacket_vals)
    elif type_id == 1:
        val = functools.reduce(lambda x, y: x * y, subpacket_vals)
    elif type_id == 2:
        val = min(subpacket_vals)
    elif type_id == 3:
        val = max(subpacket_vals)
    elif type_id == 5:
        val = 1 if subpacket_vals[0] > subpacket_vals[1] else 0
    elif type_id == 6:
        val = 1 if subpacket_vals[0] < subpacket_vals[1] else 0
    elif type_id == 7:
        val = 1 if subpacket_vals[0] == subpacket_vals[1] else 0
    return val


def get_next_packet1(s):
    version = int(s[:3], 2)
    type_id = int(s[3:6], 2)

    # print("-" * 50)
    # print("Version:", version)
    # print("Type ID:", "literal" if type_id == 4 else "operator")

    if type_id == 4:
        # literal
        literal_string = s[6:]
        start = 0
        num = ""
        is_last = 0
        while not is_last:
            group = literal_string[start : start + 5]
            is_last = 1 - int(group[0])
            num += group[1:]
            if is_last:
                # print(s[: start + 5 + 6])
                return s[: start + 5 + 6]
            else:
                start += 5
    else:
        # operator
        length_type_id = s[6]
        if length_type_id == "0":
            # print(s[:22])
            return s[:22]
        else:
            # print(s[:18])
            return s[:18]


def get_next_packet2(s):
    version = int(s[:3], 2)
    type_id = int(s[3:6], 2)

    # print("-" * 50)
    # print("Version:", version)
    # print("Type ID:", "literal" if type_id == 4 else "operator")

    if type_id == 4:
        # literal
        literal_string = s[6:]
        start = 0
        num = ""
        is_last = 0
        while not is_last:
            group = literal_string[start : start + 5]
            is_last = 1 - int(group[0])
            num += group[1:]
            if is_last:
                # print(s[: start + 5 + 6])
                return s[: start + 5 + 6], int(num, 2)
            else:
                start += 5
    else:
        # operator
        length_type_id = s[6]
        if length_type_id == "0":
            subpacket_bits = int(s[7:22], 2)
            num_bits_parsed = 0
            subpackets = s[22:]
            subpacket_vals = []
            while num_bits_parsed < subpacket_bits:
                subpacket, subpacket_val = get_next_packet2(subpackets)
                subpacket_vals.append(subpacket_val)
                subpackets = subpackets[len(subpacket) :]
                num_bits_parsed += len(subpacket)

            val = process_subpacket_vals(subpacket_vals, type_id)

            return s[: 22 + subpacket_bits], val

        else:
            # print(s[:18])
            num_subpackets = int(s[7:18], 2)
            subpackets = s[18:]
            subpacket_lengths = []
            subpacket_vals = []
            for _ in range(num_subpackets):
                subpacket, subpacket_val = get_next_packet2(subpackets)
                subpacket_vals.append(subpacket_val)
                subpackets = subpackets[len(subpacket) :]
                subpacket_lengths.append(len(subpacket))

            val = process_subpacket_vals(subpacket_vals, type_id)

            return s[: 18 + sum(subpacket_lengths)], val


if __name__ == "__main__":
    with open("data/day16.txt") as f:
        raw = f.read()

    packet_string = parse_hex(raw, hex_lookup)

    packets = []
    while sum([int(x) for x in list(packet_string)]):
        next_packet = get_next_packet1(packet_string)
        packets.append(next_packet)
        packet_length = len(next_packet)
        packet_string = packet_string[packet_length:]

    print("Part 1", sum([int(x[:3], 2) for x in packets]))

    packet_string = parse_hex(raw, hex_lookup)

    print("Part 2:", get_next_packet2(packet_string)[1])
