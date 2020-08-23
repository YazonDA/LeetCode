class Solution:
    def singleNonDuplicate(self, nums) -> int:
        while len(nums) > 2:
            print(f'question == {nums}')
            middle = len(nums) // 2 
            middle += middle % 2
            print(f'middle == {middle}: nums[:middle] == {nums[:middle]}')
            print(f'nums[middle-2] == {nums[middle-2]}; nums[middle-1] == {nums[middle-1]}')
            if nums[middle-2] == nums[middle-1]:
                nums = nums[middle:]
            else:
                nums = nums[:middle]
            print(f'ans == {nums}\n')
        print(f'answer == {nums[0]}')

a = Solution
print(a.singleNonDuplicate(a, [1,1,2,2,3,3,4,4,8,9,9]))

'''
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Input: nums = [3,3,7,7,10,11,11]
Output: 10'''