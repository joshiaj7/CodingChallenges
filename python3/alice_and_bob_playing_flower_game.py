class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        ans = 0
        if n == 1 and m == 1:
            return 0

        odd1 = n // 2
        even1 = n // 2

        if n % 2 == 1:
            odd1 += 1
    
        odd2 = m // 2
        even2 = m // 2

        if m % 2 == 1:
            odd2 += 1

        return odd1 * even2 + odd2 * even1
        