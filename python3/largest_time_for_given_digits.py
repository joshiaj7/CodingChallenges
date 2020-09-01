from itertools import permutations 

# leetcode

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        ans = ""
        perms = permutations(A) 

        # print(perms)
        for i in list(perms): 
            if (((i[0] == 2 and i[1] <= 3) or i[0] < 2) and i[2] < 6):
                temp = "{}{}:{}{}".format(i[0], i[1], i[2], i[3])
                if ans < temp:
                    ans = temp

        return ans
        