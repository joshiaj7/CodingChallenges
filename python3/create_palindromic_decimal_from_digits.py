# codility SN

def solution(S):
    ans = ""
    N = 10

    num_map = {}
    all_ones = True
    for c in S:
        i = int(c)
        if i not in num_map:
            num_map[i] = 1
        else:
            num_map[i] += 1

        if num_map[i] > 1:
            all_ones = False

    if all_ones:
        for i in range(N-1, -1, -1):
            if i in num_map:
                return str(i)

    def insert_odd(s, c, occur):
        mid = len(s) // 2
        left = s[:mid]
        right = s[mid+1:]
        middle = s[mid:mid+1]
        
        return left + (c * occur) + middle + (c * occur) + right 

    def insert_even(s, c, occur):
        mid = len(s) // 2
        left = s[:mid]
        right = s[mid:]
        
        return left + (c * occur) + right 

    for i in range(N-1, -1, -1):
        if i in num_map and num_map[i] > 0:
            if ans == "":
                if i == 0:
                    ans = "0"
                else:
                    ans = str(i) * num_map[i]
                continue

            if len(ans) == 1 and i == 0:
                continue

            if len(ans) % 2 == 0:
                ans = insert_even(ans, str(i), num_map[i])
            else:
                ans = insert_odd(ans, str(i), num_map[i] // 2)

    return ans
