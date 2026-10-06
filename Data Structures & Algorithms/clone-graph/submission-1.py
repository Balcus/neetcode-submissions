"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# DFS.
# Time Complexity: O(V + E),
# Space Complexity: O(V).

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        nodeMap = {}
        
        def dfs(node):
            nonlocal nodeMap

            if node in nodeMap or not node:
                return
    
            nodeMap[node] = Node(node.val)

            for neigh in node.neighbors:
                if neigh not in nodeMap:
                    dfs(neigh)

                nodeMap[node].neighbors.append(nodeMap[neigh])
        
        dfs(node)
        return nodeMap[node]
            