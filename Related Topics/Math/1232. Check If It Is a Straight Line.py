class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if not coordinates or len(coordinates) < 2:
            return False
        elif len(coordinates) == 2:
            return True
        
        coordinates.sort(key=lambda x: (x[0], x[1]))
        # sorted(coordinates, key=lambde x: (x[0], x[1]))
        x1, y1 = coordinates[0]
        x0, y0 = coordinates[1][0] - x1, coordinates[1][1] - y1
        
        for i in range(2, len(coordinates)):
            if y0 * (coordinates[i][0] - x1) != x0 * (coordinates[i][1] - y1):
                return False
            
        return True