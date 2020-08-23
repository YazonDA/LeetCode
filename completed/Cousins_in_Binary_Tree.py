# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
it's no my solution, because
i was can't complete this task, because
i can't understand this task

class Solution:
    def siblings(self, root: TreeNode, a:int, b:int):
        if root is None:
            return 0
        if(root.left and root.right):
            left = root.left.val
            right = root.right.val
            if((left == a and right == b) or (left == b and right == a)):
                return True
        return (self.siblings(root.left, a, b) or self.siblings(root.right, a, b))

    def height(self,root: TreeNode, x: TreeNode, h):
        if root is None:
            return 0
        if root.val == x:
            return h
        l = max(self.height(root.left, x, h+1), self.height(root.right, x, h+1))
        return l

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        #print(self.siblings(root, x, y))
        if(self.height(root, x, 0) == self.height(root, y, 0) and (not(self.siblings(root, x, y)))):
            return True
        else:
            return False
'''

def isCousins(root, x, y) -> bool:
    def _range(val):
        j = 0
        while val > (2 ** j) - 1: j += 1
        return j
    x = root.index(x) + 1
    y = root.index(y) + 1
    if x > y: x, y = y, x
    if x - y == 1 and y % 2:
        return False
    return _range(x) == _range(y) and _range(x) > 2


null = 0
a = [[[1,2,3,4], 4, 3], [[1,2,3,null,4,null,5], 5, 4], [[1,2,3,null,4], 2, 3]]
for ask in a:
	print(f'a == {ask}\n\t ==> answer == {isCousins(ask[0], ask[1], ask[2])}')
# isCousins(a, b, c)
'''
Input: a = [1,2,3,4], b = 4, c = 3
Output: false
Example 2:


Input: a = [1,2,3,null,4,null,5], b = 5, c = 4
Output: true
Example 3:



Input: a = [1,2,3,null,4], b = 2, c = 3
Output: false
'''