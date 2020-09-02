# python3

from random import randint


def partition3(array, left, right):
    x = array[left]
    j = left
    m2 = 0

    for i in range(left + 1, right + 1):
        if array[i] < x:
            j += 1
            array[j], array[i] = array[i], array[j]
        elif array[i] == x:
            m2 += 1
            j += 1
            array[j], array[i] = array[i], array[j]

    counter = left
    while counter < j - m2:
        if array[counter] == x:
            array.pop(counter)
            array.insert(j, x)
            counter -= 1

        counter += 1

    # print(x)
    # print(array)
    return [j-m2,j]


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)

    array[left], array[k] = array[k], array[left]
    m = partition3(array, left, right)
    m1 = m[0]
    m2 = m[1]


    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)

# while True:
#     randList = []
#     for i in range(10):
#         randList.append(randint(0,10))
#     print(randList)
#     trueSorted = sorted(randList)
#     randomized_quick_sort(randList, 0, len(randList) - 1)
#     if trueSorted!=randList:
#         print(False)
#         print(randList)
#         print(trueSorted)
#
#         break
#     else:
#         print(True)





if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
