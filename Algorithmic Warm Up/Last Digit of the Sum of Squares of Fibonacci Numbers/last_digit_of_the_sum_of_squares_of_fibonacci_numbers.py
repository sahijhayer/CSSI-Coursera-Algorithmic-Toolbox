# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18
    n = (n % 60) + 1
    value = 1
    fibList = [0]
    for i in range(n):
        fibList.append(int(str(value)[-1]))
        value += fibList[i]
    return int(str(fibList[-1]*fibList[-2])[-1])

if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
