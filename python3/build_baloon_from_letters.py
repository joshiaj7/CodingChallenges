"""
"BALLOONBALLOON" -> return 2
"BALLOONBALLXXN" -> return 1
"ASDFEDDL" -> return 0
"""


def solution(S):
    ans = 0
    truthmap = {
        'B': 1,
        'A': 1,
        'L': 2,
        'O': 2,
        'N': 1,      
    }
    hashmap = {}
    
    for i in S:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1
          
    exist = True
    while exist:
        for key, val in truthmap.items():
            if key in hashmap:
                if hashmap[key] - val >= 0:
                    hashmap[key] -= val
                else:
                    exist = False
                    break
            else:
                exist = False
        if exist:
            ans += 1
    
    return ans

print(solution("BALLOONBALLOONXXBALON"))
print(solution("ALEMEN"))
