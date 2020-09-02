# python3
import math

def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binarySearch(A, low, high, key):
    if high < low:
        return -1

    mid = math.floor(low + (high-low)/2)

    if key == A[mid]:
        return mid
    elif key < A[mid]:
        return binarySearch(A, low, mid - 1, key)
    else:
        return binarySearch(A, mid + 1, high, key)

def binary_search(keys, query):
    assert 1 <= len(keys) <= 3 * 10 ** 4

    return binarySearch(keys, 0, len(keys)-1, query)












if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
