# python3
import math
def edit_distance(first_string, second_string):
    distList = []
    for i in range(len(first_string)+1):
        distList.append([])
        for j in range(len(second_string)+1):
            distList[i].append(-1)
    for i in range(len(first_string)+1):
        distList[i][0] = i

    for j in range(len(second_string)+1):
        distList[0][j] = j

    for i in range(1, len(first_string) + 1):
        for j in range(1, len(second_string) + 1):
            insertion = distList[i][j-1] + 1
            deletion = distList[i-1][j] + 1
            match = distList[i-1][j-1]
            mismatch = distList[i-1][j-1] + 1

            if first_string[i-1] == second_string[j-1]:
                distList[i][j] = min(insertion, deletion, match)
            else:
                distList[i][j] = min(insertion, deletion, mismatch)
    return distList[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
