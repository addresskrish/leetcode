class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        self.visited = set()
        for i in range(len(equations)):
            graph[equations[i][0]][equations[i][1]] = float(values[i])
            graph[equations[i][1]][equations[i][0]] = float(1/values[i])

        self.answer = -1
        

        def dfs(current: str, destination: str, currentValue: float) -> None:
            if current in self.visited:
                return
            self.visited.add(current)
            if current == destination:
                self.answer = currentValue
                return 
            for neighbor in graph[current]:
                dfs(neighbor, destination, currentValue * graph[current][neighbor])
        
        
        finalAns = []

        for query in queries:
            dividend, divisor = query

            if dividend not in graph or divisor not in graph:
                finalAns.append(-1.0)
            else:
                self.visited = set()
                self.answer = -1
                temp = 1.0
                dfs(dividend, divisor, 1.0)
                finalAns.append(self.answer)

        return finalAns