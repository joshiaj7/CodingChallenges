


class Solution:

    """
    Space   : O(n)
    Time    : O(n)
    """
    def bestClosingTime(self, customers: str) -> int:
        penalties = []
        n = len(customers)
        cum_N_from_left = [0 for _ in range(n)]
        cum_Y_from_right = [0 for _ in range(n)]

        for i, v in enumerate(customers):
            # populate N cum_N_from_left 
            if i == 0:
                cum_N_from_left[i] = int(v == "N")
            else:
                cum_N_from_left[i] = cum_N_from_left[i-1] + int(v == "N")

            # populate Y cum_Y_from_right 
            if i == 0:
                cum_Y_from_right[~i] = int(customers[~i] == "Y")
            else:
                cum_Y_from_right[~i] = cum_Y_from_right[~i+1] + int(customers[~i] == "Y")

        cum_N_from_left = [0] + cum_N_from_left
        cum_Y_from_right = [cum_Y_from_right[0]] + cum_Y_from_right
        
        min_penalty = float('inf')
        for j in range(n + 1):
            if j == 0:
                penalties.append(cum_Y_from_right[j+1])
            elif j == n:
                penalties.append(cum_N_from_left[j])
            else:
                penalties.append(cum_N_from_left[j] + cum_Y_from_right[j+1])
            min_penalty = min(min_penalty, penalties[-1])

        for i, v in enumerate(penalties):
            if v == min_penalty:
                return i

        return -1
    

    """
    Space   : O(1)
    Time    : O(n)
    """
    def bestClosingTimeBest(self, customers: str) -> int:
        pre = customers.count('Y')
        least = pre
        ans = 0

        for i, v in enumerate(customers):
            if v == 'Y':
                pre -= 1
            else:
                pre += 1

            if pre < least:
                ans = i + 1
                least = pre

        return ans

