# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: list) -> 'Node':
        self.grid = grid

        root = self.divide(0, len(self.grid[0]) - 1, 0, len(self.grid) - 1)
        return root

    def divide(self, x1, x2, y1, y2):
        if x1 == x2:
            return Node(self.grid[y1][x1], True, None, None, None, None)
        else:
            node = Node(True, False, None, None, None, None)
            node.topLeft = self.divide(x1, (x1 + x2) // 2, y1, (y1 + y2) // 2)
            node.topRight = self.divide((x1 + x2) // 2 + 1, x2, y1, (y1 + y2) // 2)
            node.bottomLeft = self.divide(x1, (x1 + x2) // 2, (y1 + y2) // 2 + 1, y2)
            node.bottomRight = self.divide((x1 + x2) // 2 + 1, x2, (y1 + y2) // 2 + 1, y2)
            if node.topLeft.isLeaf and node.topRight.isLeaf and node.bottomLeft.isLeaf and node.bottomRight.isLeaf and \
                    node.topLeft.val == node.topRight.val == node.bottomLeft.val == node.bottomRight.val:
                return Node(self.grid[y1][x1], True, None, None, None, None)

            return node