from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        if rows == 0:
            return image
        cols = len(image[0])
        
        original_color = image[sr][sc]

        if original_color == color:
            return image
            
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
                return
            
            image[r][c] = color
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image
    
image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

solver = Solution()
image_recolored = solver.floodFill(image, 1, 1, 2)

for r in image:
    print(r)