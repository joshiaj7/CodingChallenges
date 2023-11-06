from heapq import heapify, heappop, heappush

class SeatManager:

    def __init__(self, n: int):
        self.seat = [i+1 for i in range(n)]
        heapify(self.seat)

    def reserve(self) -> int:
        return heappop(self.seat)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.seat, seatNumber)
