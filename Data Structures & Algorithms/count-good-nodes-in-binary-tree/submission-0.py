# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_good_node):
            if not node:
                return 0
            good = 1 if node.val>=max_good_node else 0
            max_good_node = max(node.val,max_good_node)
            return good+ dfs(node.left,max_good_node)+dfs(node.right,max_good_node)
        return dfs(root, float('-inf'))