from collections import defaultdict


class Solution:
    # personal attempt
    # memory limit exceeded
    # using DP
    # Space : O(n!)
    # Time  : O(n!)
    def countVowelPermutation(self, n: int) -> int:
        def permute(path, count):
            if count == 0:
                self.ans += 1
                return 1
            elif path and (path[-1], count) in self.dp:
                self.ans += self.dp[(path[-1], count)]
                return self.dp[(path[-1], count)]
            else:
                if not path:
                    for c in ['a', 'e', 'i', 'o', 'u']:
                        self.dp[('', count)] += permute(c, count-1)
                    return self.dp[('', count)]
                else:
                    last = path[-1]
                    if last == 'a':
                        self.dp[('a', count)] += permute(path + 'e', count-1)
                    elif last == 'e':
                        self.dp[('e', count)] += permute(path + 'a', count-1)
                        self.dp[('e', count)] += permute(path + 'i', count-1)
                    elif last == 'i':
                        self.dp[('i', count)] += permute(path + 'a', count-1)
                        self.dp[('i', count)] += permute(path + 'e', count-1)
                        self.dp[('i', count)] += permute(path + 'o', count-1)
                        self.dp[('i', count)] += permute(path + 'u', count-1)
                    elif last == 'o':
                        self.dp[('o', count)] += permute(path + 'i', count-1)
                        self.dp[('o', count)] += permute(path + 'u', count-1)
                    elif last == 'u':
                        self.dp[('u', count)] += permute(path + 'a', count-1)
                    return self.dp[(path[-1], count)]

        self.ans = 0
        self.dp = defaultdict(int)
        permute('', n)
        return self.ans % 1000000007

    # best solution
    # Space : O(1)
    # Time  : O(n)
    def countVowelPermutationBest(self, n: int) -> int:
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(n-1):
            a, e, i, o, u = e, a + i, a + e + o + u, i + u, a
        return (a + e + i + o + u) % 1000000007
