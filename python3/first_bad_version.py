"""
Space   : O(1)
Time    : O(log n)
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n

        while(low <= high):
            mid = (low + high) // 2
            if not isBadVersion(mid):
                if low != mid:
                    low = mid
                else:
                    low = mid + 1
            elif isBadVersion(mid):
                if not isBadVersion(mid-1) and isBadVersion(mid):
                    return mid
                else:
                    high = mid
