class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = defaultdict(lambda : [])
        
        for a, b in connections:
            g[a].append([b, 1])   # direction out
            g[b].append([a, 0]) 
                    
        def traverse(node, prev_node=None, cnt_changes=0) ->int:                
            for next_node, direction in g[node]:
                if next_node == prev_node:
                    continue                
                cnt_changes += direction + traverse(next_node, node)
                                
            return cnt_changes

        return traverse(0)