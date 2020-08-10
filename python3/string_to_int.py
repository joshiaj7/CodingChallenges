class Solution:
    def myAtoi(self, strt: str) -> int:
        clean_str = strt.strip()
        isNeg = False
        
        if len(clean_str) == 0:
            return 0
        
        if ((ord(clean_str[0]) < 48) or (ord(clean_str[0]) > 57)) and (clean_str[0] not in ["+", "-"]):
            return 0
        
        print(clean_str)
        
        if clean_str[0] == "-":
            isNeg = True
            clean_str = clean_str[1:]
        elif clean_str[0] == "+":
            clean_str = clean_str[1:]
        
        if len(clean_str) == 0:
            return 0
        
        print(clean_str)
        
        idx = 0
        str_ans = ''
        print(len(clean_str))
        
        for l in clean_str:
            if ord(l) >= 48 and ord(l) <= 57:
                str_ans += l
            else:
                break

        if len(str_ans) == 0:
            return 0
                
        ans = int(str_ans)
    
        if isNeg:
            ans *= -1
            
        
        if ans < (-1 * 2**31):
            return -1 * 2**31
        elif ans > ((2**31)-1):
            return (2**31)-1

    
        return ans
        