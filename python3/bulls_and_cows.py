class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        hashmap = {}
        A, B = 0, 0
        guess = list(guess)

        for x in secret:
            if x not in hashmap:
                hashmap[x] = 1
            else:
                hashmap[x] += 1

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
                hashmap[secret[i]] -= 1
                guess[i] = 'x'

        for y in guess:
            if y == 'x':
                continue
            if y in hashmap:
                if hashmap[y] > 0:
                    hashmap[y] -= 1
                    B += 1

        return "{}A{}B".format(A, B)
