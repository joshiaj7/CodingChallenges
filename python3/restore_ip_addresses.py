"""
Space   : O(2^n)
Time    : O(2^n)
"""

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        check = set()

        def dfs(i, path):
            if i == len(s):
                ip = ".".join(path)
                if len(path) == 4 and ip not in check:
                    ans.append(".".join(path))
                    check.add(ip)
            else:
                if path:
                    # if latest digit is 0
                    if path[-1] == "0":
                        dfs(i + 1, path + [s[i]])
                    # if we can append next digit to latest digit
                    elif int(path[-1] + s[i]) <= 255:
                        dfs(i + 1, path + [s[i]])
                        newpath = path[:]
                        newpath[-1] += s[i]
                        dfs(i + 1, newpath)
                    else:
                        dfs(i + 1, path + [s[i]])
                else:
                    dfs(i + 1, path + [s[i]])
                    

        dfs(0, [])
        return ans
