"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

# BFS
# Time Complexity: O(V + E)
# Space Complexity: O(V)

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        q = deque()

        # use a node map to make sure nodes are not duplicated
        nodeMap = {node: Node(node.val)}

        q.append(node)

        while q:
            # get the current node, add each neighbour to the map and q and then to the node's neighbors
            cur = q.popleft()
            for neigh in cur.neighbors:
                if neigh not in nodeMap:
                    nodeMap[neigh] = Node(neigh.val)
                    q.append(neigh)
                nodeMap[cur].neighbors.append(nodeMap[neigh])
        
        return nodeMap[node]
