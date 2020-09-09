class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(x) for x in version1.split(".")]
        v2 = [int(x) for x in version2.split(".")]
        dif = len(v1) - len(v2)

        # v2 is bigger
        if dif < 0:
            v1.extend([0] * abs(dif))
        # v1 is bigger
        elif dif > 0:
            v2.extend([0] * abs(dif))

        assert len(v1) == len(v2)

        for i in range(len(v1)):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1

        return 0
