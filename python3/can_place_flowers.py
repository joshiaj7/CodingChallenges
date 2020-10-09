"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        room1, room2 = 0, 0
        leng = len(flowerbed)
        pos1, pos2 = flowerbed.copy(), flowerbed.copy()

        if n == 0:
            return True

        if leng == 1:
            if flowerbed[0] == 0:
                return True
            else:
                return False

        i = 0
        while i < leng:
            if i == 0:
                # forward
                if pos1[i] == 0 and pos1[i+1] == 0:
                    pos1[i] = 1
                    room1 += 1

                # backward
                if pos2[leng-i-1] == 0 and pos2[leng-i-2] == 0:
                    pos2[leng-i-1] = 1
                    room2 += 1

            elif i < leng-1:
                # forward
                if pos1[i] == 0 and pos1[i-1] == 0 and pos1[i+1] == 0:
                    pos1[i] = 1
                    room1 += 1

                # backward
                if pos2[leng-i-1] == 0 and pos2[leng-i-2] == 0 and pos2[leng-i] == 0:
                    pos2[leng-i-1] = 1
                    room2 += 1

            elif i == leng-1:
                # forward
                if pos1[i] == 0 and pos1[i-1] == 0:
                    pos1[i] = 1
                    room1 += 1
                # backward
                if pos2[leng-i-1] == 0 and pos2[leng-i] == 0:
                    pos2[leng-i-1] = 1
                    room2 += 1

            i += 1

        if n <= max(room1, room2):
            return True

        return False
