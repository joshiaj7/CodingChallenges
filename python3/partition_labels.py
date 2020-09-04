class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ans = []
        indmap = {}
        leng = len(S)
        
        for i, l in enumerate(S):
            indmap[l] = i
        
        start, end = 0, 0
        
        for idx in range(leng):
            end = max(end, indmap[S[idx]])
            # print(idx, end, end-start+1)
            if idx == end:
                ans.append(end-start+1)
                start = end+1
        
        return ans