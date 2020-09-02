# python3
import math
import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
}

def min_and_max(i,j, op, m, M):
    minimum = math.inf
    maximum = -math.inf

    for k in range(i, j):

        a = ops[op[k]](M[k][i],M[j][k+1])
        b = ops[op[k]](M[k][i],m[j][k+1])
        c = ops[op[k]](m[k][i],M[j][k+1])
        d = ops[op[k]](m[k][i],m[j][k+1])
        if min(a,b,c,d) < minimum:
            minimum = min(a,b,c,d)

        if max(a,b,c,d) > maximum:
            maximum = max(a,b,c,d)
    return(minimum,maximum)


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    numbers = []
    operations = []

    for i in range(0,len(dataset)-2,2):
        numbers.append(int(dataset[i]))
        operations.append(dataset[i+1])
    numbers.append(int(dataset[-1]))
    m = []
    M = []

    for i in range(len(numbers)):
        m.append([])
        M.append([])
        for j in range(len(numbers)):
            m[i].append(0)
            M[i].append(0)

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                m[i][j] = numbers[i]
                M[i][j] = numbers[i]
    for s in range(len(numbers)-1):
        for i in range(len(numbers) - s - 1):
            j = i + s + 1
            m[j][i],M[j][i] = min_and_max(i, j, operations, m, M)

    return M[-1][0]

if __name__ == "__main__":
    print(find_maximum_value(input()))

