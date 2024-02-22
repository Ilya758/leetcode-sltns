from collections import *


class Solution:
	def isPossible(self, nums: list[int]) -> bool:
		if len(nums) < 3: return False

		frequency = Counter(nums)
		subsequence = defaultdict(int)

		for i in nums:
			if frequency[i] == 0:
				continue

			frequency[i] -= 1		

			if subsequence[i-1] > 0:
				subsequence[i-1] -= 1
				subsequence[i] += 1
			elif frequency[i+1] and frequency[i+2]:
				frequency[i+1] -= 1
				frequency[i+2] -= 1
				subsequence[i+2] += 1
			else:
				return False

		return True
	
print(Solution().isPossible(nums = [1,2,3,3,4,4,5,5])) # True