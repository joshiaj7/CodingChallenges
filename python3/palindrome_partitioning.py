class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def dfs(path, ss):
            if not ss:
                ans.append(path)
                return
            for i in range(1, len(ss)+1):
                if ss[:i] == ss[:i][::-1]:
                    dfs(path + [ss[:i]], ss[i:])

        dfs([], s)
        return ans
