# in [1, 1, 4, 1, 2, 4]
# expectation (1, 4), (2, 4), (1, 1)
# out 
# pick a pair with neigbor with the highest pair 3 times
# return the sum


def solution(A):
    ans = 0

    k = 3
    while k > 0 and len(A) > 1:
        max_pair_idx = -1
        max_pair_sum = 0

        for i in range(len(A)-1):
            if A[i] + A[i+1] > max_pair_sum:
                max_pair_sum = A[i] + A[i+1]
                max_pair_idx = i

        ans += max_pair_sum
        A = A[:max_pair_idx] + A[max_pair_idx+2:]
        k -= 1
        
    return ans
