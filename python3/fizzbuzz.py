# leetcode

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        
        for i in range(1, n+1):
            word = ''
            
            if i % 3 == 0:
                word += 'Fizz'
            if i % 5 == 0:
                word += "Buzz"
            if word == '':
                word = str(i)
            ans.append(word)
        
        print(ans)
        return ans