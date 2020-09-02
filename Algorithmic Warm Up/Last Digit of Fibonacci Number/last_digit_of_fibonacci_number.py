# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10

def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7


    value = 0
    fibList = [1]
    for i in range(n):
        fibList.append(int(str(value)[-1]))
        value += fibList[i]
    return int(str(value)[-1])


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
