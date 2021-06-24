# Space : O(n)
# Time  : O(n)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        hashmap = {numbers[i]: (i+1) for i in range(n)}

        for i in range(n):
            if target - numbers[i] in hashmap:
                return [i+1, hashmap[target - numbers[i]]]

        return []
