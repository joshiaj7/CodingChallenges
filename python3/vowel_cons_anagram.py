"""
Vowel and Consonant Anagram Problem

Example S = "BALE"
letter count
B = 1
A = 1
L = 1
E = 1

Solution:
Consonant = 2! / 1! 1!
Vowel = 2! / 1! 1!
Result = Consonant * Vowel

Example S = "BABALEK"
letter count
B = 2
K = 1
L = 1
A = 2
E = 1

Solution:
Consonant = 4! / 2! 1! 1! 1!
Vowel = 3! / 2! 1!
Result = Consonant * Vowel
"""

def get_factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def get_con_div(hashmap):
    res = 1
    for key, val in hashmap.items():
        if key not in ['A', 'E', 'I', 'O', 'U']:
            res *= get_factorial(val)
    return res

def get_vow_div(hashmap):
    res = 1
    for key, val in hashmap.items():
        if key in ['A', 'E', 'I', 'O', 'U']:
            res *= get_factorial(val)
    return res

def solution(S):
    vow = 0
    con = 0
    hashmap = {}
    for l in S:
        if l in ['A', 'E', 'I', 'O', 'U']:
            vow += 1
        else:
            con += 1
        if l not in hashmap:
            hashmap[l] = 1
        else:
            hashmap[l] += 1

    if con - vow not in [0, 1]:
        return 0

    # print(vow, con, hashmap)

    res_con = (get_factorial(con)) / get_con_div(hashmap)
    res_vow = (get_factorial(vow)) / get_vow_div(hashmap)

    return int(res_con * res_vow) % 1000000007


res = solution("BOLOBOLO")
print("res : {}".format(res))