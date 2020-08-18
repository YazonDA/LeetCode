#class Solution:
def majorityElement(nums) -> int:
	char, number = '', 0
	for i in nums:
		if char != i and number < nums.count(i):
			char, number = i, nums.count(i)
	return char


a = [3,2,3]
# a = [2,2,1,1,1,2,2]

print(f'a == {a} ==> answer == {majorityElement(a)}')