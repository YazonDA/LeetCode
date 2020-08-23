class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        ansL = 0
        ansR = 2 ** 31 - 1
        while num != ansL ** 2 and num != ansR **2:
            if ansR - ansL == 1:
                return False
            suppose = (ansR + ansL) // 2
            if suppose ** 2 > num:
                ansR = suppose
            else:
                ansL = suppose
            print(f'num {num}\tansL {ansL}\tansR {ansR}')
        return True


a = Solution
print(a.isPerfectSquare(a, 1))


'''
Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false
'''