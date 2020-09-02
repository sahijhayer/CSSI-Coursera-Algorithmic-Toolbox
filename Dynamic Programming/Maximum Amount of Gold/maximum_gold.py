# python3

from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    value = []
    solutions = []

    for i in range(len(weights)+1):
        value.append([])
        solutions.append([])
        for j in range(capacity+1):
            value[i].append(0)
            solutions[i].append(0)
    for i in range(1, len(weights) + 1):
        for w in range(1, capacity + 1):
            value[i][w] = value[i-1][w]
            solutions[i][w] = solutions[i-1][w]
            if weights[i-1] < w+1:
                val = solutions[i-1][w-weights[i-1]]+ weights[i-1]
                if solutions[i][w] < val :
                    solutions[i][w] = solutions[i-1][w-weights[i-1]] + weights[i-1]

    print(solutions[-1][-1])


# capacity = int(input())
# weights = list(map(int, input().split()))
# maximum_gold(capacity, weights)

if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
