#7.7: Recursion

def sumList(nums):
	if len(nums) == 1:
		return nums[0]
	return nums[0] + sumList(nums[1:])

def sumToN(n):
	if n < 1:
		return 0
	return n + sumToN(n - 1)

def NxN(n, n0):
	if n < 2:
		return [0 for i in range(n0)]
	return [NxN(n - 1, n0) for i in range(n0)]
