# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majorityElement(elements, low, high):
    if len(elements[low:high]) == 2:
        if elements[low:high][0] == elements[low:high][1]:
            return elements[low:high][0]
        else:
            return 0

    if len(elements[low:high]) == 3:
        if elements[low:high][0] == elements[low:high][1] or elements[low:high][0] == elements[low:high][2]:
            return elements[low:high][0]
        elif elements[low:high][1] == elements[low:high][2]:
            return elements[low:high][1]
        else:
            return 0

    a = majorityElement(elements,(low+high)//2, high)
    b = majorityElement(elements, low, (low+high)//2)

    counterA = 0
    counterB = 0


    if a == -1 and b == -1:
        return 0

    if a != -1:
        for i in range(len(elements[low:high])):
            if elements[low+i] == a:
                counterA += 1
    if b != -1:
        for i in range(len(elements[low:high])):
            if elements[low+i] == b:
                counterB += 1
    if counterA > len(elements[low:high]) / 2:
        return a
    elif counterB > len(elements[low:high]) / 2:
        return b
    else:
        return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5

    if majorityElement(elements,0,len(elements)) != 0:
        return 1
    else:
        return 0



if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
