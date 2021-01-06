class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        Personal attempt
        Space   : O(1)
        Time    : O(n)
        """

        n = len(arr)     
        ans = 0
        
        for i in range(n):
            if i == 0:
                if arr[i] <= k:
                    k -= arr[i] - 1
                    continue
                else:
                    ans = k
                    k = 0
                    break
            
            dif = arr[i] - arr[i-1]
            if dif <= k:
                k = k - dif + 1
            else:
                ans = arr[i-1] + k
                k = 0
                break
                            
        
        if k > 0:
            ans = arr[-1] + k
        
        return ans

    def findKthPositiveBest(self, arr: List[int], k: int) -> int:
        """
        Best solution
        Space   : O(1)
        Time    : O(log n)
        """
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) //2
            if arr[mid] - (mid + 1) < k:
                left = mid + 1
            else:
                right = mid - 1
        return left + k