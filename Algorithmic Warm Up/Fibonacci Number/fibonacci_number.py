# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)

def fibonacci_number(n):
    fibList = [0]
    modList = ["0"]
    value = 1
    for i in range(n):
        fibList.append(value)
        modList.append(str(value%3))
        value += fibList[i]
    return modList


print(''.join(fibonacci_number(100)))




#if __name__ == '__main__':
    #input_n = int(input())
    #print(fibonacci_number(input_n))
