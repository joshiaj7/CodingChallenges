from collections import defaultdict

"""
Space   : O(nm)
Time    : O(nm)
n = len(paths)
m = len(paths[i])
"""


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = []
        file_map = defaultdict(list)

        for p in paths:
            p = p.split(' ')
            directory = p[0]
            files = p[1:]
            for f in files:
                f = f.split('(')
                filename = f[0]
                content = f[-1][:-1]
                file_map[content].append(directory + '/' + filename)

        for _, v in file_map.items():
            if len(v) > 1:
                ans.append(v)

        return ans
