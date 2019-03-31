# -*- coding: utf-8 -*-
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root and root.val > val:
            return self.searchBST(root.left, val)
        elif root and root.val < val:
            return self.searchBST(root.right, val)
        return root
