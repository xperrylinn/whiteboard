# Calculate the Nth Fibonacci number, where:
# Fibonacci number: 0   1   2   3   4   6   7
#                   0   1   1   2   3   5   8

# Recursive solution. 
def getNthFib(n):
    # Write your code here.
    if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return getNthFib(n - 1) + getNthFib(n - 2)
# Notes:
#   -   O(2^n) time | O(n) space
#   --  each recursive makes two recursive calls, recursive calls are repeated,
#       i.e. fib(5) calls fib(4) and fib(4), fib(4) also calls fib(3), etc..
#   --  n space because of recursive calls on the stack

# Iterative Solution.
def getNthFib(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	
	one, two = 0, 1
	n -= 2
	
	while (n > 1):
		temp = two
		two += one
		one = temp
		n -= 1
	
	return one + two
# Notes:
#   -   O(n) time | O(1) space
#   --  Looping roughly n times
#   --  No additional space needed


# Memoized recursive solution
def getNthFib(n, memoize={1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n-1, memoize) + getNthFib(n-2, memoize)
        return memoize[n]
# Notes:
#   - O(n) time | O(n) space