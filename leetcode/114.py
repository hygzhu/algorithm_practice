"""
Given a binary tree, flatten it to a linked list in-place.
"""

#Beats 99.87% of python submissions
class Solution:
    def recursiveFlatten(self, node, root):
        """
        :type root: TreeNode
        :rtype: the new root
        """
        if node == None:
            return root
        
        leftChild = node.left
        rightChild = node.right
        
        root.left = None
        root.right = node
        
        newRoot = self.recursiveFlatten(leftChild, node)
        return self.recursiveFlatten(rightChild, newRoot)
    
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        if root == None:
            return root
        
        leftChild = root.left
        rightChild = root.right
        
        root.left = None
        
        newRoot = self.recursiveFlatten(leftChild, root)
        self.recursiveFlatten(rightChild, newRoot)
        