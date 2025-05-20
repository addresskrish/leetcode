class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        n = len(isConnected)
        adj = defaultdict(set)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    adj[i].add(j)
                    adj[j].add(i)
        res = 0
        for i in range(n):
            if i not in visited:
                queue = [i]
                res += 1
            while queue:
                node = queue.pop(0)
                for neighor in adj[node]:
                    if neighor in visited:
                        continue
                    queue.append(neighor)
                    visited.add(neighor)
        return res