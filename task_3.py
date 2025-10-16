class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        def dfs(v):
            # Помечаем вершину как посещенную
            visited[v] = True
            # Проверяем всех соседей
            for neighbor in range(n):
                # Если есть связь и сосед еще не посещен
                if isConnected[v][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        for v in range(n):
            if not visited[v]:
                provinces += 1
                # DFS для всех городов провинции
                dfs(v)
        return provinces
