import math

from typing import List 
def twoSum(nums: List[int], target: int) -> List[int]:
	for idx in range(math.ceil(len(nums) /2)):
		expected_num = target - nums[idx]
		try:
			expected_idx = nums.index(expected_num,idx+1)
			if idx != expected_idx:
				print([idx, expected_idx])
				return
			else:
				continue
		except:
			return 
	

# nums = [2,7,11,15]
# target = 9
nums = [3,3]
target = 6
twoSum(nums,target)