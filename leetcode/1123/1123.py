from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def postorder_traversal(node: Optional[TreeNode], depth: int):
            if not node:
                return (None, depth)
            
            left_lca, left_depth = postorder_traversal(node.left, depth+1)
            right_lca, right_depth = postorder_traversal(node.right, depth+1)

            if left_depth > right_depth:
                return (left_lca, left_depth)
            elif right_depth > left_depth:
                return (right_lca, right_depth)
            else:
                return (node, left_depth)

        lca, _ = postorder_traversal(root, 0)

        return lca