def solve(dolls):
    ans = 0
    N = len(dolls)

    if N == 0:
        return ans

    hashmap = {}

    for i in dolls:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1

    for k, v in hashmap.items():
        ans = max(ans, v)

    return ans


print(solve([1, 2, 2, 3, 4, 5]))
print(solve([1, 2, 2, 4, 4, 4, 4, 5]))
print(solve([1, 10, 10, 100, 10000, 10000,
             10000, 20000, 20000, 20000, 20000, 20000]))
