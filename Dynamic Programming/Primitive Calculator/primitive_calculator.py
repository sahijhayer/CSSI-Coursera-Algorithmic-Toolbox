# python3
import operator

def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.xor,
    }

    options = [["-",1],["/",2],["/",3]]
    operations = [0]
    sequences = [[]]
    for i in range(1, n+1):
        operations.append(float("inf"))
        sequences.append([])
        for j in range(len(options)):
            check = ops[options[j][0]](i,options[j][1])
            if float(check).is_integer():
                newNum = operations[int(check)] + 1
                if newNum < operations[i]:
                    operations[i] = newNum
                    sequences[i] = sequences[int(check)].copy()
                    sequences[i].append(i)

    return sequences[n]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
