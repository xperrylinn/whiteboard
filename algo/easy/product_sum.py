# Write a function that returns the product sum of a nested list of ints
# Example: array = []

def productSum(array):
    # Write your code here.
    return helper(array)

def helper(array, depth=1):
	result = 0
	for elem in array:
		if not isinstance(elem, int):
			elem = helper(elem, depth + 1)
		result += (elem * depth)
	return result