import re


def get_distance_between(sensor, beacon):
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])


def get_min_max_non_beacon_point_in_row(sensor, dist, rownum, xrange=None):

    x = sensor[0]
    y = sensor[1]

    ydist = abs(y - rownum)

    if ydist > dist:
        return []
    else:
        min_point = (x - (dist - ydist), rownum)
        max_point = (x + (dist - ydist), rownum)

        if xrange:
            min_point = (min(min_point[0], xrange[1]), rownum)
            max_point = (min(max_point[0], xrange[1]), rownum)

            min_point = (max(min_point[0], xrange[0]), rownum)
            max_point = (max(max_point[0], xrange[0]), rownum)

        return [min_point, max_point]


def get_num_non_beacon_points_in_row(sensors, beacons, rownum):
    min_max = {}
    for i in range(len(sensors)):
        dist = get_distance_between(sensors[i], beacons[i])
        min_max[sensors[i]] = get_min_max_non_beacon_point_in_row(
            sensors[i], dist, rownum
        )

    non_beacon_points = []
    for s in min_max:
        if min_max[s]:
            non_beacon_points = non_beacon_points + list(
                range(min_max[s][0][0], min_max[s][1][0] + 1)
            )

        non_beacon_points = list(set(non_beacon_points))
    return len([p for p in non_beacon_points if (p, rownum) not in beacons])


def search_row(sensors, beacons, rownum):
    min_max = {}
    for i in range(len(sensors)):
        dist = get_distance_between(sensors[i], beacons[i])
        min_max[sensors[i]] = get_min_max_non_beacon_point_in_row(
            sensors[i], dist, rownum, xrange=(0, 4000000)
        )

    sensor_ranges = sorted(list({k: v for k, v in min_max.items() if v}.values()))

    next_start = sensor_ranges[0][0][0]
    assert next_start == 0
    covered_up_to = sensor_ranges[0][1][0]

    for i in range(len(sensor_ranges) - 1):
        end = sensor_ranges[i][1][0]
        next_start = sensor_ranges[i + 1][0][0]

        if end == 4000000:
            break
        if next_start <= end and end >= covered_up_to:
            covered_up_to = end
        elif next_start > end + 1 and next_start > covered_up_to + 1:
            if next_start == end + 1 and (end + 1, rownum) not in beacons:
                continue
            else:
                return (end + 1, rownum)


if __name__ == "__main__":
    with open("data/day15.txt") as f:
        coords = [x.strip() for x in f.readlines()]

    sensors = []
    beacons = []

    for c in coords:
        sensor_pos = re.findall("-?\d+", c.split(":")[0])
        sensors.append((int(sensor_pos[0]), int(sensor_pos[1])))

        becaon_pos = re.findall("-?\d+", c.split(":")[1])
        beacons.append((int(becaon_pos[0]), int(becaon_pos[1])))

    print("Part 1:", get_num_non_beacon_points_in_row(sensors, beacons, 2000000))

    for i in range(4000000):
        found = search_row(sensors, beacons, i)
        if found:
            break

    print("Part 2:", found[0] * 4000000 + found[1])
