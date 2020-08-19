# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
def isCousins(root, x, y) -> bool:
	pass


null = 0
# a = [1,2,3,4]
# b = 4
# c = 3
# a = [1,2,3,null,4,null,5]
# b = 5
# c = 4
a = [1,2,3,null,4]
b = 2
c = 3

print(f'a == {a, b, c}\n\t ==> answer == {isCousins(a, b, c)}')

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