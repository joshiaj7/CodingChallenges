"""
Space   : O(n)
Time    : O(1)
"""


class UndergroundSystem:

    def __init__(self):
        self.passenger_hash = {}
        self.avg_station = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passenger_hash[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        origin, start_time = self.passenger_hash[id]

        pair = (origin, stationName)
        if pair in self.avg_station:
            avg, freq = self.avg_station[pair]
            new_avg = ((avg * freq) + (t - start_time)) / (freq + 1)
            self.avg_station[pair] = (new_avg, freq + 1)
        else:
            self.avg_station[pair] = ((t - start_time), 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.avg_station[(startStation, endStation)][0]
