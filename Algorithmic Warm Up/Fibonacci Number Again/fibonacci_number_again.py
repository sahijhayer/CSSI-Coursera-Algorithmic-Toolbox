# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current



def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
    fibList = [0]
    modList = [0]
    value = 1
    i = 0

    while True:
        fibList.append(value)
        modList.append(value%m)
        value += fibList[i]
        if modList[i] == 1 and modList[i-1] == 0 and i > 2:
            break
        i += 1

    return modList[n%(i-1)]



if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
