# TreeNode definition (LeetCode format)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution class
class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


if __name__ == "__main__":
    # Tạo cây tương ứng với [1,2,3,4,5,6]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    sol = Solution()
    result = sol.countNodes(root)
    print("nombre de node ", result)
