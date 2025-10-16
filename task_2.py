class Solution(object):
    def maxAreaOfIsland(self, grid):
        # получаем размеры сетки
        rows, cols = len(grid), len(grid[0])
        
        # алгоритм вычисления площади
        def DFS(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0 # помечаем как "просмотренную"
            area = 1
            # рекурсивно вызываем функция для проверки соседних значений 
            area += DFS(r+1, c)
            area += DFS(r-1, c)
            area += DFS(r, c+1)
            area += DFS(r, c-1)
            return area
        
        max_area = 0 # начальная "максимальная" площадь
        # проходимся по всем значениям матрицы
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1: # если встретили "сушу" запускаем DFS
                    max_area = max(max_area, DFS(i, j))
        
        return max_area
    

# Пример использования 
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(Solution().maxAreaOfIsland(grid))
# Ответ: 6

    
