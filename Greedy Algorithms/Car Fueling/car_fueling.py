# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    newStops = stops
    newStops.insert(0,0)
    newStops.append(d)
    i = 0
    refills = 0
    num_stops = len(newStops)
    if d <= m:
        return 0
    while i < num_stops:
        current = i
        if d - stops[i] <= m:
            return refills
        while (stops[i + 1]-stops[current]) <= m:

            i += 1
            if i == num_stops - 1:
                break

        if current == i:
            return -1
        if i < num_stops:
            refills += 1

    return refills


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
