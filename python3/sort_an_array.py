"""
Space   : O(n)
Time    : O(n log n)
"""


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                left_arr = arr[:mid]
                right_arr = arr[mid:]

                mergeSort(left_arr)
                mergeSort(right_arr)

                i = j = k = 0

                while i < len(left_arr) and j < len(right_arr):
                    if left_arr[i] < right_arr[j]:
                        arr[k] = left_arr[i]
                        i += 1
                    else:
                        arr[k] = right_arr[j]
                        j += 1
                    k += 1

                while i < len(left_arr):
                    arr[k] = left_arr[i]
                    i += 1
                    k += 1
                
                while j < len(right_arr):
                    arr[k] = right_arr[j]
                    j += 1
                    k += 1

            return arr
            
        return mergeSort(nums)
