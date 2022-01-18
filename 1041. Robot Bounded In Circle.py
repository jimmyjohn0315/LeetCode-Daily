class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [ [0, 1]
                     ,[1, 0]
                     ,[0, -1]
                     ,[-1, 0]
                     ]
        d = 0
        x, y = 0, 0
        for i in instructions:
            if i == 'R':
                d = (d + 1) % 4
            elif i == 'L':
                d = (d - 1) % 4
            elif i == 'G':
                x += directions[d][0]
                y += directions[d][1]
        
        return x == y == 0 or d != 0
