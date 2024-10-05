from typing import List

# Space : O(1)
# Time  : O(n * m)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        coord = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows = len(image)
        cols = len(image[0])
        start = image[sr][sc]
        
        def crawl(x, y):
            if image[y][x] == start:
                image[y][x] = newColor
            for fy, fx in coord:
                if x+fx == -1 or x+fx == cols or y+fy == -1 or y+fy == rows:
                    continue
                if image[y+fy][x+fx] != start or image[y+fy][x+fx] == newColor:
                    continue
                crawl(x+fx, y+fy)
                    
        crawl(sc, sr)
        return image    
        
        