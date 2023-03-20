"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count, place = 0, 0
        all_zero = True
        beginning = flowerbed[0] == 0
        leng = len(flowerbed)

        if n == 0:
            return True

        for i in range(leng):
            if flowerbed[i] == 0:
                count += 1
            else:
                all_zero = False
                if beginning:
                    place += count // 2
                    beginning = False
                elif count > 0:
                    place += (count - 1) // 2
                count = 0

        if all_zero:
            return (leng+1) // 2 >= n
                
        if count > 0:
            place += count // 2

        return place >= n
