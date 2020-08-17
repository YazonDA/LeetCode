# class Solution:
def firstUniqChar(s: str) -> int:
	print(f'len(s) == {len(s)}')
	for i in range(len(s)):
		print(f'i == {i}; s[i] == {s[i]}')
		print(f's.count(s[i]) == {s.count(s[i])}')
		if s.count(s[i]) - 1:
			return i
	return -1

a = 'leetcode'
print(f'{a} == {firstUniqChar(a)}')