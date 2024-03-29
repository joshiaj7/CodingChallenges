"""
Space   : O(n)
Time    : O(nm)
"""


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        ans = set()
        for word in words:
            morse = ''
            for i in word:
                morse += code[ord(i)-97]
            ans.add(morse)

        return len(ans)
