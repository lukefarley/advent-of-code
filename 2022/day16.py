import re
import itertools
from collections import deque


def shortest_path_length(graph, start, end):

    if start == end:
        return 0

    visited = []

    q = deque()
    q.append([start])

    while q:
        path = q.popleft()
        node = path[-1]

        if node not in visited:
            neighbors = graph[node]

            for neighbor in neighbors:
                q.append(list(path) + [neighbor])

                if neighbor == end:
                    return len(path)

        visited.append(node)


if __name__ == "__main__":

    with open("data/day16.txt") as f:
        valves = [x.strip() for x in f.readlines()]

    valve_names = [v[6:8] for v in valves]
    flow_rates = [int(re.findall("\d+", v)[0]) for v in valves]

    leads_to_valves = []
    for v in valves:
        if "lead to valves" in v:
            leads_to_valves.append(v.split("lead to valves ")[1].split(", "))
        else:
            leads_to_valves.append(v.split("leads to valve ")[1].split(", "))

    valve_flow_rates = dict(zip(valve_names, flow_rates))
    valve_leads_to = dict(zip(valve_names, leads_to_valves))

    # flow_rates_leads_to = dict(zip(valve_names, [[valve_flow_rates[ltv] for ltv in ltvs] for ltvs in leads_to_valves]))

    all_pairs = [
        p for p in list(itertools.product(valve_names, valve_names)) if p[0] != p[1]
    ]

    distance_mapping = {}
    for i, pair in enumerate(all_pairs):
        print(i)
        distance_mapping[(pair[0], pair[1])] = shortest_path_length(
            valve_leads_to, pair[0], pair[1]
        )

    non_zero_flow_rates = {k: v for k, v in valve_flow_rates.items() if v > 0}
    non_zero_flow_valves = list(non_zero_flow_rates.keys())

    ##################
    # Part 1
    ##################

    total_minutes = 30
    minutes_passed = 0

    node_name = "AA"
    pressure = 0

    q = deque()
    q.append(([node_name], minutes_passed, pressure))

    max_pressure = 0

    # do bfs until we've reached a path of length 30
    while q:

        current_node = q.popleft()

        path = current_node[0]
        current_valve = path[-1]

        minutes_passed = current_node[1]
        pressure = current_node[2]

        if pressure > max_pressure:
            max_pressure = pressure

        for option in [valve for valve in non_zero_flow_valves if valve not in path]:
            mins = minutes_passed + distance_mapping[(current_valve, option)] + 1
            presh = pressure + valve_flow_rates[option] * (total_minutes - mins)

            # if path == ["AA", "DD", "BB", "JJ", "HH", "EE"]:
            #     stop()
            #     print(path + [option])
            total_mins_left = total_minutes - mins
            remaining_flow_rates = list(
                reversed(
                    sorted(
                        [
                            valve_flow_rates[valve]
                            for valve in non_zero_flow_valves
                            if valve not in path + [option]
                        ]
                    )
                )
            )
            num_valves_can_visit = min(total_mins_left // 2, len(remaining_flow_rates))
            hypothetical_presh = presh
            # if remaining_flow_rates:
            for i in range(num_valves_can_visit):
                # if i <= len(remaining_flow_rates) - 1:
                hypothetical_presh += remaining_flow_rates[i] * (
                    total_mins_left - 2 * i
                )

            if hypothetical_presh >= max_pressure:
                q.append((path + [option], mins, presh, hypothetical_presh))
            # q.append((path + [option], mins, presh))

            # q.append((path + [option], mins, presh))

        q = deque([node for node in q if node[1] < 30])
        q = deque(reversed(sorted(q, key=lambda x: x[-1])))

    print("Part 1:", max_pressure)

    ##################
    # Part 2
    ##################

    total_minutes = 26
    minutes_passed = 0

    node_name = "AA"
    pressure = 0

    q = deque()
    q.append(([node_name], 0, 0, [node_name], 0, 0))

    max_pressure = 0

    while q:

        current_node = q.popleft()

        my_path = current_node[0]
        my_valve = my_path[-1]
        my_minutes_passed = current_node[1]
        my_pressure = current_node[2]

        elephant_path = current_node[3]
        elephant_valve = elephant_path[-1]
        elephant_minutes_passed = current_node[4]
        elephant_pressure = current_node[5]

        if my_pressure + elephant_pressure > max_pressure:
            max_pressure = my_pressure + elephant_pressure

        if my_minutes_passed <= elephant_minutes_passed:
            for option in [
                valve
                for valve in non_zero_flow_valves
                if valve not in my_path and valve not in elephant_path
            ]:
                mins = my_minutes_passed + distance_mapping[(my_valve, option)] + 1
                presh = my_pressure + valve_flow_rates[option] * (total_minutes - mins)

                my_mins_left = total_minutes - mins
                elephant_minutes_left = total_minutes - elephant_minutes_passed
                total_mins_left = 26 * 2 - mins - elephant_minutes_passed

                remaining_flow_rates = list(
                    reversed(
                        sorted(
                            [
                                valve_flow_rates[valve]
                                for valve in non_zero_flow_valves
                                if valve not in my_path + [option] + elephant_path
                            ]
                        )
                    )
                )

                num_valves_can_visit = min(
                    total_mins_left // 2, len(remaining_flow_rates)
                )
                hypothetical_presh = presh

                for i in range(num_valves_can_visit):
                    hypothetical_presh += remaining_flow_rates[i] * max(
                        elephant_minutes_left - 2 * i, my_mins_left - 2 * i
                    )

                if hypothetical_presh + elephant_pressure >= max_pressure:
                    q.append(
                        (
                            my_path + [option],
                            mins,
                            presh,
                            elephant_path,
                            elephant_minutes_passed,
                            elephant_pressure,
                            hypothetical_presh + elephant_pressure,
                        )
                    )

            # q = deque([node for node in q if len(node[0]) + len(node[3]) - 2 < 15])
            # q = deque([node for node in q if node[1] < 26 or node[4] < 26])
            q = deque(reversed(sorted(q, key=lambda x: x[-1])))

        else:
            for option in [
                valve
                for valve in non_zero_flow_valves
                if valve not in my_path and valve not in elephant_path
            ]:
                mins = (
                    elephant_minutes_passed
                    + distance_mapping[(elephant_valve, option)]
                    + 1
                )
                presh = elephant_pressure + valve_flow_rates[option] * (
                    total_minutes - mins
                )

                my_mins_left = total_minutes - my_mins_left
                elephant_minutes_left = total_minutes - mins
                total_mins_left = 26 * 2 - my_minutes_passed - mins

                remaining_flow_rates = list(
                    reversed(
                        sorted(
                            [
                                valve_flow_rates[valve]
                                for valve in non_zero_flow_valves
                                if valve not in my_path + elephant_path + [option]
                            ]
                        )
                    )
                )

                num_valves_can_visit = min(
                    total_mins_left // 2, len(remaining_flow_rates)
                )
                hypothetical_presh = presh

                for i in range(num_valves_can_visit):
                    hypothetical_presh += remaining_flow_rates[i] * max(
                        elephant_minutes_left - 2 * i, my_mins_left - 2 * i
                    )

                if hypothetical_presh + my_pressure >= max_pressure:
                    q.append(
                        (
                            my_path,
                            my_minutes_passed,
                            my_pressure,
                            elephant_path + [option],
                            mins,
                            presh,
                            hypothetical_presh + my_pressure,
                        )
                    )

        # q = deque([node for node in q if len(node[0]) + len(node[3]) - 2 < 15])
        # q = deque([node for node in q if node[1] < 26 or node[4] < 26])
        q = deque(reversed(sorted(q, key=lambda x: x[-1])))

    print("Part 2:", max_pressure)
