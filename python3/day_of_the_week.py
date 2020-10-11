"""
Space   : O(n)
Time    : O(1)
"""

from datetime import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        truth = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday",
        }

        # Monday is 0 and Sunday is 6
        date = datetime(year, month, day)

        return truth[date.weekday()]
