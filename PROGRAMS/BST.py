class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root):
    def helper(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True
        
        val = node.val
        if val <= lower or val >= upper:
            return False
        
        if not helper(node.right, val, upper):
            return False
        if not helper(node.left, lower, val):
            return False
        
        return True
    
    return helper(root)

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(is_valid_bst(root)) 
