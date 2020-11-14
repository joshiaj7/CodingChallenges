"""
Space   : O(n)
Time    : O(n)
"""

from datetime import datetime
import requests


def numDevices(statusQuery, threshold, dateStr):
    ans = 0

    s = [int(i) for i in dateStr.split('-')]
    if s[0] == 12:
        e = [0, s[1]+1]
    else:
        e = [str(s[0]+1), str(s[1])]

    date_start = datetime.strptime(dateStr, "%m-%Y")
    date_end = datetime.strptime("-".join(e), "%m-%Y")
    endpoint = "https://jsonmock.hackerrank.com/api/iot_devices/search?status={}&page={}"

    page = 1
    while True:
        response = requests.get(endpoint.format(statusQuery, page))
        data = response.json().get("data")
        if data:
            for item in data:
                date = datetime.fromtimestamp(item.get("timestamp")/1000)
                thres = item.get('operatingParams').get('rootThreshold')
                if (date >= date_start) and (date <= date_end) and (thres > threshold):
                    ans += 1
        else:
            break
        page += 1

    return ans
