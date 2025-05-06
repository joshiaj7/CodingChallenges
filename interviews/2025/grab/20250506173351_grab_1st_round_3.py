# 1 -> [1]
# 2 -> [2, 2]
# 3 -> [3, 3, 3]
# 4 -> [4, 4, 4, 4]
# ....

# insert cost = 1
# delete cost = 1

# in [1, 2, 2, 3, 3, 3, 5, 5, 5]
# expectation [1, 2, 2, 3, 3, 3]
# out 3

# in [1, 1, 1, 3, 4, 4, 4, 4]
# expectation [1, 4, 4, 4, 4]
# out 3

# in [1, 1, 1, 3, 4, 4, 4, 4]
# expectation [1, 4, 4, 4, 4]
# out 3

def solution(A):
    ans = 0
    n = len(A)

    # count occurences
    countMap = {}
    for num in A:
        if num in countMap:
            countMap[num] += 1
        else:
            countMap[num] = 1

    # delete excess
    insertArr = []
    for k, v in countMap.items():
        if v > k:
            ans += v - k
            countMap[k] = k
            insertArr.append((0, k))
        else:
            insertArr.append((k - v, k))

    insertArr.sort(key=lambda x: x[0])

    capacity = n
    for room, num in insertArr:
        # delete num from list if overcapacity
        if capacity - num < 0:
            ans += countMap[num]
        # reduce capacity and add room cost if capable
        else:
            capacity -= num
            ans += room

    return ans
