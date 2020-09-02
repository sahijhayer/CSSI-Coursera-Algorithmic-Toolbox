# python3


def lcm_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiple = max(a, b)
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1

    return multiple

def gcd(a, b):
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9
    if b > a:
        temp_a = a
        a = b
        b = temp_a
    while b != 0:
        temp = a
        a = b

        b = temp % b


    return a

def lcm(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    factor = 1
    greater = max(a,b)
    while (factor * greater) % a != 0 or (factor * greater)%b!=0:
        factor += 1
    return factor * greater

if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))
