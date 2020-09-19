class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        start, end = len(str(low)), len(str(high))
        truth = '123456789'

        for i in range(start, end+1):
            print(i)
            s = 0
            e = i
            while e < 10:
                print(truth[s:e])
                num = int(truth[s:e])
                if low <= num <= high:
                    ans.append(num)
                elif num > high:
                    break
                s += 1
                e += 1

        return ans
