from collections import defaultdict

# Space : O(n)
# Time  : O(n)
# n = number of files given

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = []
        mem = defaultdict(list)
        
        for directory in paths:
            directory = directory.split(" ")
            path = directory[0]
            files = directory[1:]
            for file in files:
                file = file.split("(")
                file_name = file[0]
                file_content = file[1][:len(file[1])-1]
                mem[file_content].append(path + '/' + file_name)
            
        for val in mem.values():
            if len(val) > 1:
                ans.append(val)
        
        return ans