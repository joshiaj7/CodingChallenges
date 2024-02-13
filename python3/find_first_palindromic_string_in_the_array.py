from typing import List

"""
Space   : O(1)
Time    : O(nm)
"""

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            i, j = 0, len(word)-1
            is_palindromic = True

            while i < j:
                if word[i] != word[j]:
                    is_palindromic = False
                    break
                i += 1
                j -= 1

            if is_palindromic:
                return word

        return ""
        