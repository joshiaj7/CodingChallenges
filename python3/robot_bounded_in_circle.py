class Solution:
    def turnRight(self, direction: str) -> str:
        if direction == "N":
            return "E"
        elif direction == "E":
            return "S"
        elif direction == "S":
            return "W"
        elif direction == "W":
            return "N"

    def turnLeft(self, direction: str) -> str:
        if direction == "N":
            return "W"
        elif direction == "W":
            return "S"
        elif direction == "S":
            return "E"
        elif direction == "E":
            return "N"

    def moveForward(self, direction: str, pos: List[int]) -> List[int]:
        if direction == "N":
            return [pos[0], pos[1]+1]
        elif direction == "E":
            return [pos[0]+1, pos[1]]
        elif direction == "S":
            return [pos[0], pos[1]-1]
        elif direction == "W":
            return [pos[0]-1, pos[1]]

    def isRobotBounded(self, instructions: str) -> bool:
        cur = "N"
        pos = [0, 0]

        for i in instructions*4:
            if i == "G":
                pos = self.moveForward(cur, pos)
            elif i == "L":
                cur = self.turnLeft(cur)
            elif i == "R":
                cur = self.turnRight(cur)

        if pos == [0, 0]:
            return True
        return False
