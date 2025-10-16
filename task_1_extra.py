def floodFill(image, sr: int, sc: int, color: int):
    start_color = image[sr][sc]
    if start_color == color:
        return image

    m, n = len(image), len(image[0])

    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n:
            return
        if image[r][c] != start_color:
            return

        image[r][c] = color
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return image
image = [[1,1,1],[1,1,0],[1,0,1]]
print(floodFill(image, 1, 1, 2))