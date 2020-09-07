class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        strl = string.split(" ")

        if len(pattern) != len(strl):
            return False

        pat_map = {}
        str_map = {}
        for idx in range(len(pattern)):
            # print(pattern[idx], string_list[idx])
            if (pattern[idx] not in pat_map) and (strl[idx] not in str_map):
                pat_map[pattern[idx]] = strl[idx]
                str_map[strl[idx]] = pattern[idx]
                # print(pat_map, str_map)
            elif pattern[idx] not in pat_map:
                return False
            elif strl[idx] not in str_map:
                return False
            else:
                if pat_map[pattern[idx]] != strl[idx] or str_map[strl[idx]] != pattern[idx]:
                    return False

        return True
