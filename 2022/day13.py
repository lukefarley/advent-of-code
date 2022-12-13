def compare_packets(p1, p2):

    for i in range(len(p1)):
        if i >= len(p2):
            # right side ran out of items
            return 0

        if type(p1[i]) == list and type(p2[i]) == list:
            val = compare_packets(p1[i], p2[i])
            if val in [0, 1]:
                return val
        elif type(p1[i]) == int and type(p2[i]) == list:
            val = compare_packets([p1[i]], p2[i])
            if val in [0, 1]:
                return val
        elif type(p1[i]) == list and type(p2[i]) == int:
            val = compare_packets(p1[i], [p2[i]])
            if val in [0, 1]:
                return val
        else:
            if p1[i] < p2[i]:
                return 1
            elif p1[i] > p2[i]:
                return 0

    if len(p1) < len(p2):
        # left side ran out of items
        return 1


# define Packet class that implements a less than method to use python's built in sorting for part 2
class Packet:
    def __init__(self, packet):
        self.packet = packet

    def __lt__(self, other):
        return compare_packets(self.packet, other.packet)


if __name__ == "__main__":

    with open("data/day13.txt") as f:
        packets = f.read().split("\n\n")

    packets = [[eval(p) for p in pair.split("\n")] for pair in packets]

    correct_order_indicators = []
    for i, p in enumerate(packets):
        correct_order_indicators.append(compare_packets(p[0], p[1]))

    print(
        "Part 1:",
        sum([i + 1 for i, val in enumerate(correct_order_indicators) if val == 1]),
    )

    all_packets = []
    for p in packets:
        all_packets.append(Packet(p[0]))
        all_packets.append(Packet(p[1]))

    # add dividers
    all_packets.append(Packet([[2]]))
    all_packets.append(Packet([[6]]))

    # sort
    sorted_packets = sorted(all_packets)

    divider_indices = [
        i + 1 for i, p in enumerate(sorted_packets) if p.packet in [[[2]], [[6]]]
    ]
    print("Part 2:", divider_indices[0] * divider_indices[1])
