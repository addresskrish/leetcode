class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]

        visited = [False for _ in range(len(rooms))]

        while stack:
            current = stack.pop()

            if not visited[current]:
                visited[current] = True
                for key in rooms[current]:
                    stack.append(key)

        return True if all(visited) else False