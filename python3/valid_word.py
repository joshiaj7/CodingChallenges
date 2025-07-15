class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        hasVowel = False
        hasConsonant = False
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])

        for l in word:
            if not (48 <= ord(l) <= 57 or 65 <= ord(l) <= 122):
                return False

            if 65 <= ord(l) <= 122:
                if l in vowels:
                    hasVowel = True
                else:
                    hasConsonant = True

        return hasVowel and hasConsonant
        