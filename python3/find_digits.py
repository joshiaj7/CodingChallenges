def findDigits(n):
    ans = 0

    num = str(n)
    leng = len(num)
    d = {}

    for i in range(leng):
        x = int(num[i])
        if x > 0:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1

    for k, v in d.items():
        if n % k == 0:
            ans += v

    return ans
