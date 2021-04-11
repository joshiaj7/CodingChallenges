# Space	: O(n)
# Time		: O(n!)


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        phone_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        n = len(digits)
        
        if not digits:
            return ans
        
        def combination(digs, path):
            if len(path) == n:
                ans.append(path)
            if len(digs) > 0:
                for letters in phone_map[digs[0]]:
                    for letter in letters:
                        combination(digs[1:], path + letter)
        
        combination(digits, "")
        
        return ans
