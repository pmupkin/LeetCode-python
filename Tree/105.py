
#######
#list.pop 默认移除最后一个元素
#list.index 从列表中找出某个值第一个匹配项的索引位置
#切片如果索引超出范围会返回[]
#######
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            index = inorder.index(preorder.pop(0))
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[:index])
            node.right = self.buildTree(preorder, inorder[index+1:])
            return node
            