from .model import Trie


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """
        Personal Attempt
        Space   : O(n)
        Time    : O(n)
        """
        if len(dictionary) == 0:
            return sentence

        hashmap = {}

        for word in dictionary:
            if word not in hashmap:
                hashmap[word] = 1
            else:
                hashmap[word] += 1

        sen = sentence.strip().split(" ")

        ans = ''

        for i in range(len(sen)):
            check = ''
            for j in range(len(sen[i])):
                check += sen[i][j]
                if check in hashmap:
                    ans += check
                    check = ''
                    break
            if check != '':
                ans += check
            if i < len(sen) - 1:
                ans += ' '

        return ans

    def replaceWords2(self, dictionary: List[str], sentence: str) -> str:
        """
        Best Solution
        Trie Method
        Space   : O(n)
        Time    : O(n)
        """
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        res = []
        for s in sentence.split():
            res.append(trie.search(s))
        return ' '.join(res)
