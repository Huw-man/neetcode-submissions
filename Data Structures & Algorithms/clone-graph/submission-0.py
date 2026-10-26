"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:

        visited = {}

        def clone(node):
            if not node:
                return None
            elif node.val in visited:
                return visited[node.val]

            c = Node(node.val)
            visited[c.val] = c

            new_neighbors = []
            for n in node.neighbors:
                new_n = clone(n)
                new_neighbors.append(new_n)

            c.neighbors = new_neighbors

            return c

        return clone(node)
