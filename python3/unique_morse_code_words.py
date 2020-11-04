"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        n = len(words)
        code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        ans = set()
        for word in words:
            morse = ''
            for i in word:
                morse += code[ord(i)-97]
            ans.add(morse)

        return len(ans)
