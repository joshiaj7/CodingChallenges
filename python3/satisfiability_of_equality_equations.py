import string

"""
Space   : O(n)
Time    : O(n)

Mehtod:
Union Find
"""


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find_parent(x):
            if d[x] != x:
                d[x] = find_parent(d[x])
            return d[x]

        # fill d with alphabets reference to themselves
        d = {a: a for a in string.ascii_lowercase}

        # check the equal nodes
        for a, e, _, b in equations:
            if e == '=':
                d[find_parent(a)] = find_parent(b)

        check = []
        # check the unequal nodes
        for a, e, _, b in equations:
            if e == '!':
                check.append(find_parent(a) == find_parent(b))

        return not any(check)
